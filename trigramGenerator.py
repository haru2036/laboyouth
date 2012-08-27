#!/usr/bin/env python
# -*- coding: utf-8 -*
import MeCab
import sys,random
import binarysearch

#此処から関数
def trigramGenerator(keyword,sentence):
	list=[]
	itemlist=[]
	m=MeCab.Tagger("-Owakati")
	for line in sentence:
		wakati = m.parse(line)
		wakatistrip=wakati.strip()
		itemlist+=wakatistrip.split(" ")
	#print itemlist
	itemlist2 = [x.decode('utf-8') for x in itemlist]
	freq1={}
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
			freq2={z:1}
			freq1[x]={y:freq2}
	sentence=[]
	sentence.append(keyword.decode("utf-8"))
	keyslist=freq1[sentence[0]].keys()
	values=len(freq1[sentence[0]].values())
	secondwords=freq1[sentence[0]].keys()
	sentence.append(secondwords[random.randint(0,len(secondwords)-1)])
	j=0
	while sentence[j]!=u"。":
		keyslist1 = freq1[sentence[j]][sentence[j+1]].keys()
		valueslist= freq1[sentence[j]][sentence[j+1]].values()
		j=j+1
		sentence.append(keyslist1[binarysearch.binarysearch(valueslist)])
		"""print "---------------------Sentence Start----------------"
		for p in sentence:
			print p
		print "---------------------Sentence End------------------"
		print j,sentence[-1]"""
	return sentence
