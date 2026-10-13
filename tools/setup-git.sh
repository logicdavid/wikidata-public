#!/bin/sh
# Run once per clone, from the repository root: sh tools/setup-git.sh
# Registers the notebook filter used in .gitattributes. Git does not copy
# filter definitions when cloning, so every collaborator has to run this.

git config filter.nbstrip.clean "python3 tools/nbstrip_filter.py"
git config filter.nbstrip.smudge cat
git config filter.nbstrip.required true
echo "Notebook filter configured."
