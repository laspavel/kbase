#!/usr/bin/env python3

import glob, os


os.chdir('../')
file_list=[]
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".md"):
             if os.path.join(root, file)!='../README.md':
                 file_list.append(os.path.join(root, file))

contents={}
for file_l in file_list:
   temp = open(file_l, "r").readlines() 
   for i in temp:
       if i.startswith('# '):
           i=i.replace('# ', '').replace(' #', '')
           file_l=file_l.replace('./','')
           if file_l in contents:
               contents[file_l].append(i)
           else:
               contents[file_l]=[i]


print(contents)
exit(0)
