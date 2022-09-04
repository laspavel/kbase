#!/usr/bin/env python3

from pathlib import Path

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
                    tree_str.append({'type': 'file', 'level': n, 'name': i, 'path': str(
                        pathname.resolve()).replace(str(base_path.as_posix())+'/', '')})
    elif pathname.is_dir() and pathname.name != ".git":
        tree_str.append({'type': 'dir', 'level': n, 'name': str(
            pathname.relative_to(pathname.parent)), 'path': str(pathname.resolve()).replace(str(base_path.as_posix())+'/', '')})
        open(str(pathname.resolve())+'/README.md', "w+")
        for cp in pathname.iterdir():
            generate_tree(cp, n + 1)


if __name__ == '__main__':
    base_path = Path.cwd()
    generate_tree(base_path / 'src')
    for data in tree_str:
        if data['type'] == 'dir':
            with open(data['path']+'/README.md', "w") as outf:
                for ds in tree_str:
                    if ds['path'].find(data['path']) > -1:
                        outf.write(
                            " " * 4 * (ds['level']-data['level']) + '* '"[" + ds['name'] + "](" + ds['path'] + ") "  "\n")

    with open('README.md', "w") as lf:
        lf.write("# База знаний # " + "\n")
        with open('src/README.md', "r") as lb:
            for lineb in lb:
                lf.write(lineb)
