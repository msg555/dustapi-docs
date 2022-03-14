#!/usr/bin/env python3

import argparse
import collections
import re
import sys

from pyparsing import (
    c_style_comment,
    dbl_slash_comment,
    delimited_list,
    Opt,
    StringEnd,
    SkipTo,
    White,
    Literal,
    Group,
    Word,
    Forward,
    ZeroOrMore,
    alphas,
    alphanums,
)


ref_type = Literal("&in") | Literal("&out")
identifier = Word(alphas + "_", alphanums + "_") 

type_identifier = Forward()
type_identifier <<= Group(
    identifier("type_name") +
    Opt(Literal("<") + delimited_list(type_identifier)("sub_types") + ">") +
    Opt("@")("ref")
)

single_arg = Group(Opt(Literal("const"))("const") + type_identifier("arg_type") + Opt(ref_type)("ref_type") + Opt(identifier("arg_name")))
arg_list = Opt(delimited_list(single_arg)("args"))

comment = c_style_comment | dbl_slash_comment

function_body = Forward()
function_body <<= Group((Literal("{") +
    (SkipTo(Literal("/*") | "//" | "{", fail_on=Literal("}")) + (comment | function_body))[...] +
    SkipTo(Literal("}"), fail_on=Literal("/*") | "//" | "{") +
    "}"
))

(Opt(comment | function_body) + SkipTo(comment | "}" | "{"))[...] + Literal("}")

function_definition = Group(
    (type_identifier("func_type") + identifier("func_name") | identifier("func_name")) +
    "(" + arg_list("func_args") + ")" +
    (Literal(";") | function_body("func_body"))
)


variable_definition = Group(Opt(Literal("[") + SkipTo("]") + "]") + type_identifier("var_type") + delimited_list(identifier)("var_names") + Literal(";"))
class_member = variable_definition("class_var") | function_definition("class_func")

class_definition = Group(
    Literal("class") + identifier("class_name") + Opt(Literal(":") + delimited_list(identifier)("base_types")) +
    "{" +
    Group(comment("comment") | class_member("class_member"))[...]("class_parts") +
    "}"
)

document = Group(comment("comment") | class_definition("classdef") | ";")[...]("docparts")


def strip_text(text):
    START_TEXT = "/* STARTAPI */"
    STOP_TEXT = "/* STOPAPI */"

    pos = 0
    chunks = []
    while True:
        pos = text.find(START_TEXT, pos)
        if pos == -1:
            break
        pos += len(START_TEXT)

        epos = text.find(STOP_TEXT, pos)
        if epos == -1:
            chunks.append(text[pos:])
            break

        chunks.append(text[pos:epos])
        pos = epos + len(STOP_TEXT)


    return "".join(chunks)


def mangle_refs(line, ref_context=None):
    ref_context = ref_context or {}
    def repl(m):
        name = m.group(2)
        if m.group(1) == "class":
            return f"\\ :ref:`{name}<class-{name}>`\\ "
        elif m.group(1) in ("func", "function"):
            return f"\\ :ref:`{name}<func-{name}>`\\ "
        elif m.group(1) in ("meth", "method"):
            parts = name.split(".", 1)
            if len(parts) == 1:
                return f"\\ :ref:`{name}<method-{ref_context.get('class', '')}-{name}>`\\ "
            else:
                return f"\\ :ref:`{name}<method-{'-'.join(parts)}>`\\ "
        return m.group(0)

    return re.sub(r":([a-z]+):`([a-zA-Z_:.]+)`", repl, line)


def emit_comment(out, indent, comment, ref_context=None):
    leading_spaces = None
    for comment_line in comment.split("\n"):
        comment_line = comment_line.strip()
        if comment_line.endswith("*/"):
            comment_line = comment_line[:-2]
        if comment_line.startswith("//"):
            comment_line = comment_line[2:]
        elif comment_line.startswith("/*"):
            comment_line = comment_line[2:]
        elif comment_line.startswith("*"):
            comment_line = comment_line[1:]

        if leading_spaces is None:
            leading_spaces = 0
            while leading_spaces < len(comment_line) and comment_line[leading_spaces] == " ":
                leading_spaces += 1
            if leading_spaces == len(comment_line):
                leading_spaces = None
                continue

        if comment_line:
            if not comment_line.startswith(" " * leading_spaces):
                sys.stderr.write(f"{comment} {comment_line}\n")
                raise ValueError("unexpected comment indentation")

            comment_line = comment_line[leading_spaces:]
        out.write(f"{indent}{mangle_refs(comment_line, ref_context=ref_context)}\n")
    out.write("\n")


def strip_prefix(identifier, prefix):
    if identifier.startswith(prefix):
        return identifier[len(prefix):]
    return identifier


def format_type_identifier(type_id, name_override=None):
    type_id = type_id[0]
    type_name = name_override or type_id.type_name
    if type_id.sub_types:
        return "**{}**\\<{}>{}".format(
            type_name,
            ", ".join(format_type_identifier(sub_type) for sub_type in type_id.sub_types),
            type_id.ref,
        )

    type_ref = f"**{type_name}**"
    if type_name.startswith("int") or type_name.startswith("uint") or type_name.endswith("_base"):
        pass
    elif type_name not in ("void", "float", "string", "bool"):
        type_ref = f":ref:`{type_name}<class-{type_name}>`"

    return f"\\ {type_ref}\\ {type_id.ref}"


def format_arg(arg, type_name_override=None):
    const = "const " if arg.const else ""
    ref_type = arg.ref_type + " " if arg.ref_type else ""
    return f"{const}{format_type_identifier(arg.arg_type, name_override=type_name_override)} {ref_type}{arg.arg_name}"


def format_arg_list(arg_list):
    if isinstance(arg_list, str):
        # Matches as a blank str when empty
        return ""
    return ", ".join(format_arg(arg) for arg in arg_list)


def bite_func_name_chunk(name):
    pos = 0
    while True:
        pos = name.find("_", pos)
        if pos == -1:
            raise ValueError("no more chunks to bite!")
        if pos + 1 < len(name) and name[pos + 1] == "_":
            pos += 2
            continue

        return name[pos + 1:], name[:pos].replace("__", "_")


def emit_funcdef(out, indent, funcdef, parent_name, comment, name_ctr, prefix):
    if not funcdef.func_type:
        # Functions without return types are constructors which we don't
        # want to generate docs for.
        return

    func_name = strip_prefix(funcdef.func_name, prefix)
    func_type = funcdef.func_type
    if func_name.startswith("ret_"):
        func_name, return_type = bite_func_name_chunk(func_name[4:])
        func_type = type_identifier.parse_string(return_type + "@")

    args = []
    for arg in funcdef.func_args:
        type_name_override = None
        if arg.arg_type[0].type_name.startswith("hx_"):
            func_name, type_name_override = bite_func_name_chunk(func_name)

        args.append(format_arg(arg, type_name_override=type_name_override))

    name_ctr[func_name] += 1
    label_suffix = ""
    if name_ctr[func_name] > 1:
        label_suffix = f"-{name_ctr[func_name]}"
    
    if parent_name:
        out.write(f"{indent}.. _method-{parent_name}-{func_name}{label_suffix}:\n\n")
    else:
        out.write(f"{indent}.. _func-{func_name}{label_suffix}:\n\n")

    func_def_line = f"{format_type_identifier(func_type)} " \
                    f"*{func_name}*\ ({', '.join(args)})"
    out.write(f"{indent}{func_def_line}\n\n")
    if comment:
        emit_comment(
            out,
            indent + "  ",
            comment,
            ref_context={
                "class": parent_name,
                "func": func_name,
            },
        )


def emit_classdef(out, indent, classdef, comment, prefix):
    base_types = set(strip_prefix(base_type, prefix) for base_type in classdef.base_types)
    base_types.discard("linked_script_object")

    class_name = strip_prefix(classdef.class_name, prefix)

    out.write(f"{indent}.. _class-{class_name}:\n\n")
    out.write(f"{indent}class {class_name}\n")
    out.write(indent + "#" * (len(class_name) + 6) + "\n")

    if len(base_types) == 1:
        base_type = next(iter(base_types))
        out.write(f"{indent}  Inherits: `{base_type} <#class-{base_type}>`_\n\n")
    elif base_types:
        out.write(f"{indent}  Inherits:\n")
        for base_type in base_types:
            out.write(f"{indent}    `{base_type} <#class-{base_type}>`_\n\n")

    if comment:
        emit_comment(out, indent + "  ", comment)

    emit_class_members(out, indent + "  ", classdef, class_name, prefix)


def emit_class_members(out, indent, classdef, class_name, prefix):
    name_ctr = collections.Counter()
    last_comment = None
    for part in classdef.class_parts:
        if part.comment:
            last_comment = part.comment
        if part.class_func and part.class_func.func_name.startswith(prefix):
            emit_funcdef(out, indent, part.class_func, class_name, last_comment, name_ctr, prefix)
            last_comment = None


def main():
    parser = argparse.ArgumentParser(description="Preprocess documentation into RST")
    parser.add_argument(
        "--prefix",
        default="",
        required=False,
        help="Required class/method name prefix to be included",
    )
    args = parser.parse_args()

    text = sys.stdin.read()
    text = strip_text(text)
    
    result = document.parse_string(text, parse_all=True)
    last_comment = None
    for part in result.docparts:
        if part.comment:
            last_comment = part.comment
            continue

        if not part.classdef:
            continue
        if part.classdef.class_name == "user_script":
            if last_comment:
                emit_comment(sys.stdout, "" + "  ", last_comment)
                last_comment = None
            emit_class_members(sys.stdout, "", part.classdef, "", args.prefix)
            continue
        if not part.classdef.class_name.startswith(args.prefix):
            continue

        emit_classdef(sys.stdout, "", part.classdef, last_comment, args.prefix)
        last_comment = None


if __name__ == "__main__":
    main()
