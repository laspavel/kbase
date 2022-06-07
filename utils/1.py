#!/usr/bin/env python3

from pathlib import Path

tree_str = ''

def generate_tree(pathname, n=0):
    global tree_str
    if pathname.is_file():
        if pathname.name.endswith(".md"):
           tree_str += '#' * n + pathname.name + '\n'
    elif pathname.is_dir():
        tree_str += '#' * n + \
            str(pathname.relative_to(pathname.parent)) + '\\' + '\n'
        for cp in pathname.iterdir():
            generate_tree(cp, n + 1)

if __name__ == '__main__':
    generate_tree(Path.cwd().parent)
    print(tree_str)