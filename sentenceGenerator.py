#!/usr/bin/env python
# -*- coding: utf-8 -*
import binarysearch
import random
class sentenceGenerator:
	def __init__(self,freq1,keyword):
		self.freq1=freq1
		self.keyword=keyword
	def generateSentence(self):
		sentence=[]
		sentence.append(self.keyword.decode("utf-8"))
		if self.keyword.decode("utf-8") not in self.freq1:
			sentence.append("えっと……わからないや、ごめんね")
			sentence.append("Error1")
		else:
			keyslist = self.freq1[sentence[0]].keys()
			values=self.freq1[sentence[0]].values()
			y=keyslist[random.randint(0,len(keyslist)-1)]
			sentence.append(y)
			j=0
			while sentence[j]!=u"。":
				if sentence[j] not in self.freq1:
					sentence.append("……えっと……途中まで考えてたんだけど忘れちゃった。ごめんね")
					sentence.append("Error2")
				else:
					keyslist1=self.freq1[sentence[j]][sentence[j+1]].keys()
					valueslist=self.freq1[sentence[j]][sentence[j+1]].values()
					j=j+1

					x=keyslist1[binarysearch.binarysearch(valueslist)]
					sentence.append(x)
			return sentence
