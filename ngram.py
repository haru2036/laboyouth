#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MeCab
import sys,random
import codecs

sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
list = []
itemlist=[]
m=MeCab.Tagger("-Owakati")
for line in sys.stdin:
    wakati =  m.parse(line)
    itemlist+=wakati.split(" ")
#print itemlist
itemlist2 = [x.decode('utf-8') for x in itemlist]
print itemlist2[0]
"""
f=codecs.open("wakati.txt",'w','utf-8')
for x in itemlist:
    f.write(x.decode('utf-8'))
    f.write("\n")
f.close()
"""
freq = dict()
for x in itemlist2:
    if x in freq:
        freq[x]+=1
    else:
        freq[x]=1
for x in freq:
    print "%s : %d" %(x,freq[x])
