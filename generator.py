#!/usr/bin/env python3

from pathlib import Path
from sys import builtin_module_names

tree_str = []


def generate_tree(pathname, n=0):
    global tree_str
    global base_path
    if pathname.is_file():
        if pathname.name.endswith(".md"):
            temp = open(str(pathname.resolve()), "r").readlines()
            for i in temp:
                if i.startswith('# '):
                    i = i.replace('# ', '').rstrip()
                    tree_str.append(
                        {'type': 'file', 'level': n, 'name': i, 'path': str(pathname.resolve()).replace(str(base_path.as_posix())+'/', '')})
    elif pathname.is_dir() and pathname.name != ".git":
        tree_str.append({'type': 'dir', 'level': n, 'name': str(
            pathname.relative_to(pathname.parent)), 'path': str(pathname.resolve()).replace(str(base_path.as_posix())+'/', '')})
        for cp in pathname.iterdir():
            generate_tree(cp, n + 1)


if __name__ == '__main__':
    base_path = Path.cwd()
    generate_tree(base_path / 'src')
    with open('README.md', "w") as lf:
        lf.write("# База знаний # " + "\n")
        for data in tree_str:
            lf.write(" " * 4 * data['level'] + '* '
                     "[" + data['name'] + "](" + data['path'] + ") "  "\n")
