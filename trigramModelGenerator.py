#!/usr/bin/env python
# -*- coding: utf-8 -*
import MeCab

class trigramModelGenerator:
	def __init__(self,sentence):
		self.sentence=sentence
	def generateModel(self):
		itemlist=[]
		m=MeCab.Tagger("-Owakati")
		for line in self.sentence:
			wakati = m.parse(line)
			wakatistrip=wakati.strip()
			itemlist+=wakatistrip.split(" ")
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
		return freq1
