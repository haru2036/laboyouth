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
#print itemlist2[0]
"""
f=codecs.open("wakati.txt",'w','utf-8')
for x in itemlist:
    f.write(x.decode('utf-8'))
    f.write("\n")
f.close()
"""
freq1 = {}
for i in xrange(len(itemlist2)-1):
    x=itemlist2[i]
    y=itemlist2[i+1]
    if x in freq1:
        if y in freq1[x]:
            freq1[x][y]+=1
        else:
            freq1[x][y]=1
    else:
        freq1[x]={y:1}        
for x in freq1:
    print "%s : %s" %(x,freq1[x])
    for y in freq1[x]:
        print"%s:%d"%(y,freq1[x][y])
