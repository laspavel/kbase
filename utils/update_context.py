#!/usr/bin/env python3

import glob, os

os.chdir('../')
file_list=[]
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".md"):
             if os.path.join(root, file)!='./README.md':
                 file_list.append(os.path.join(root, file))

ds={}
for file_l in file_list:
   temp = open(file_l, "r").readlines() 
   for i in temp:
       if i.startswith('# '):
           i=i.replace('# ', '').replace(' #', '').rstrip()
           file_l=file_l.replace('./','')
           if file_l in ds:
               ds[file_l].append(i)
           else:
               ds[file_l]=[i]

contents={}
for d in ds:
    x=d.split('/')
    del x[0]
    del x[len(x)-1]

    for y in x:
        if y in contents:
            contens[y].extend({'name': d)


    print(x)


exit(0)
