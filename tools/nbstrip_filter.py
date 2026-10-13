"""Git clean filter for notebooks (see .gitattributes and tools/setup-git.sh).

Reads a notebook on stdin and writes the version git should store to stdout.

- On main:  keep outputs and execution counts (main showcases the notebooks),
            only drop kernel metadata, which differs from machine to machine.
- Elsewhere (devel, feature branches): also drop outputs and execution counts,
            so running a cell does not show up as a change.

Uses only the standard library, so it runs with any python3, independent of
the project's virtual environment.
"""
import json
import subprocess
import sys

NOTEBOOK_METADATA_TO_STRIP = ['kernelspec', 'language_info']
CELL_METADATA_TO_STRIP = ['execution', 'ExecuteTime', 'collapsed', 'scrolled']


def current_branch():
    result = subprocess.run(['git', 'symbolic-ref', '--short', '-q', 'HEAD'],
                            capture_output=True, text=True)
    return result.stdout.strip()


def strip(notebook, keep_output):
    for key in NOTEBOOK_METADATA_TO_STRIP:
        notebook.get('metadata', {}).pop(key, None)
    if keep_output:
        return notebook
    for cell in notebook.get('cells', []):
        if cell.get('cell_type') == 'code':
            cell['outputs'] = []
            cell['execution_count'] = None
        for key in CELL_METADATA_TO_STRIP:
            cell.get('metadata', {}).pop(key, None)
    return notebook


def main():
    raw = sys.stdin.buffer.read()
    try:
        notebook = json.loads(raw.decode('utf-8'))
    except ValueError:
        # Not valid JSON (e.g. during a merge conflict): store it unchanged
        sys.stdout.buffer.write(raw)
        return
    notebook = strip(notebook, keep_output=(current_branch() == 'main'))
    # Same layout as Jupyter/nbformat writes, so unchanged notebooks stay byte-identical
    text = json.dumps(notebook, sort_keys=True, indent=1, ensure_ascii=False) + '\n'
    sys.stdout.buffer.write(text.encode('utf-8'))


if __name__ == '__main__':
    main()
