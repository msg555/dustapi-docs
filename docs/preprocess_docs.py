#!/usr/bin/env python3

import collections
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


def emit_comment(out, indent, comment):
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
        out.write(f"{indent}{comment_line}\n")
    out.write("\n")


def strip_api(identifier):
    if identifier.startswith("api_"):
        return identifier[4:]
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

    return f"\\ **{type_name}**\\ {type_id.ref}"


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


def emit_funcdef(out, indent, funcdef, parent_name, comment, name_ctr):
    if not funcdef.func_type:
        # Functions without return types are constructors which we don't
        # want to generate docs for.
        return

    func_name = strip_api(funcdef.func_name)
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
        out.write(f"{indent}.. _method-{func_name}{label_suffix}:\n\n")

    out.write(f"{indent}{format_type_identifier(func_type)} ")
    out.write(f"*{func_name}*\ ({', '.join(args)})\n\n")
    if comment:
        emit_comment(out, indent + "  ", comment)


def emit_classdef(out, indent, classdef, comment):
    base_types = set(strip_api(base_type) for base_type in classdef.base_types)
    base_types.discard("linked_script_object")

    class_name = strip_api(classdef.class_name)

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

    emit_class_members(out, indent + "  ", classdef, class_name)


def emit_class_members(out, indent, classdef, class_name):
    name_ctr = collections.Counter()
    last_comment = None
    for part in classdef.class_parts:
        if part.comment:
            last_comment = part.comment
        if part.class_func:
            emit_funcdef(out, indent, part.class_func, class_name, last_comment, name_ctr)
            last_comment = None


def main():
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
            emit_class_members(sys.stdout, "", part.classdef, "")
            continue
        if not part.classdef.class_name.startswith("api_"):
            continue

        emit_classdef(sys.stdout, "", part.classdef, last_comment)
        last_comment = None


if __name__ == "__main__":
    main()
