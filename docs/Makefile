# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help preprocess Makefile html

preprocess: ../source/dustapi.hpp
	mkdir -p _build
	python3 preprocess_docs.py < _templates/script.hpp > _build/script.rst
	python3 preprocess_docs.py < _templates/trigger_base.hpp > _build/trigger_base.rst
	python3 preprocess_docs.py < _templates/enemy_base.hpp > _build/enemy_base.rst
	python3 preprocess_docs.py < ../source/dustapi.hpp > _build/dustapi.rst

html:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
