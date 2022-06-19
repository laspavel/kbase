#!/usr/bin/env python3

from pathlib import Path

tree_str = []


def generate_tree(pathname, n=0):
    global tree_str
    global level
    if pathname.is_file():
        if pathname.name.endswith(".md"):
            temp = open(str(pathname.resolve()), "r").readlines()
            for i in temp:
                if i.startswith('# '):
                    i = i.replace('# ', '').rstrip()
                    tree_str.append(
                        {'type': 'file', 'level': n, 'name': i, 'path': str(pathname.resolve())})
    elif pathname.is_dir() and pathname.name != ".git":
        tree_str.append({'type': 'dir', 'level': n, 'name': str(
            pathname.relative_to(pathname.parent)), 'path': str(pathname.resolve())})
        for cp in pathname.iterdir():
            generate_tree(cp, n + 1)


if __name__ == '__main__':
    #    generate_tree(Path('../src'))
    generate_tree(Path('/home/laspavel/_/kbase/src'))
    with open('/home/laspavel/_/kbase/README.md', "w") as lf:
        lf.write("# База знаний # " + "\n")
        for data in tree_str:
            lf.write(" " * 4 * data['level'] + '* '
                     "[" + data['name'] + "](" + data['path'] + ") "  "\n")
