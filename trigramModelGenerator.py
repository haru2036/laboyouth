#!/usr/bin/env python
# -*- coding: utf-8 -*
import mecabCaller
class trigramModelGenerator:
	def __init__(self,sentence):
		self.sentence=sentence
	def generateModel(self):
		mc=mecabCaller.mecabCaller(self.sentence)
		itemlist2=mc.parse()
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
		keyslist=freq1.keys()
		return freq1
