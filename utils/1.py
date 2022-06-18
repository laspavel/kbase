#!/usr/bin/env python3

from pathlib import Path

tree_str = []


def generate_tree(pathname, n=0):
    global tree_str
    global level
    if pathname.is_file():
        if pathname.name.endswith(".md"):
            tree_str.append({'type': 'file', 'level': n,
                            'name': pathname.name, 'path': str(pathname.resolve())})
    elif pathname.is_dir() and pathname.name != ".git":
        tree_str.append({'type': 'dir', 'level': n, 'name': str(
            pathname.relative_to(pathname.parent)), 'path': str(pathname.resolve())})
        for cp in pathname.iterdir():
            generate_tree(cp, n + 1)


if __name__ == '__main__':
    #    generate_tree(Path('../src'))
    generate_tree(Path('/home/laspavel/_/kbase/src'))
    print(tree_str)
