#!/usr/bin/env python
# -*- coding: utf-8 -*
import MeCab
import sys,random
import codecs
import binarysearch
#ここからtrigram生成
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
for i in xrange(len(itemlist2)-2):
    x=itemlist2[i]
    y=itemlist2[i+1]
    z=itemlist2[i+2]
    if x in freq1:
        if y in freq1[x]:
            if z in freq1[x][y]:
                freq1[x][y][z]+=1
            else:
                freq1[x][y][z]=1
        else:
            freq1[x][y]={z:1}
    else:
        freq2 = {}
        freq2={z:1}
        freq1[x]={y:freq2}        
for x in freq1:
    print "%s : %s" %(x,freq1[x])
    for y in freq1[x]:
        print"%s:%s"%(y,freq1[x][y])
        for z in freq1[x][y]:
            print"%s:%d"%(z,freq1[x][y][z])
sentence=[]
"""
keyslist=freq1[u"start1"].keys()
valueslist=freq1[u"start2"].values()
result=binarysearch.binarysearch(valueslist)
print result,len(keyslist)"""
sentence.append(u"ボク")
sentence.append(u"に")
i=0
while sentence[i]!=u"。":
    keyslist=freq1[sentence[i]][sentence[i+1]].keys()
    valueslist=freq1[sentence[i]][sentence[i+1]].values()
    i=i+1
    sentence.append(keyslist[binarysearch.binarysearch(valueslist)])
print u" ".join(sentence)
