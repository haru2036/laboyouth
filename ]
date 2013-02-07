#!/usr/bin/env python
# -*- coding: utf-8 -*
import binarysearch
import random
class sentenceGenerator:
	def __init__(self,freq1):
		#freq1,keywordはunicode
		self.freq1=freq1
	def generateSentence(self,keyword):
		sentence=[]
		if keyword not in self.freq1:
			sentence.append(u"えっと……わからないや、ごめんね")
			sentence.append("Error1")
			return sentence
		sentence.append(keyword)
		keyslist = self.freq1[keyword].keys()
		y=keyslist[random.randint(0,len(keyslist)-1)]
		sentence.append(y)
		j=0
#		while (sentence[j]!=(u"。" or u"？"or u"?")) or (j<=10):
		while len(sentence)<10:
			if sentence[j] not in self.freq1:
				sentence.append("……えっと……途中まで考えてたんだけど忘れちゃった。ごめんね")
				sentence.append("Error2")
				return sentence
			else:
				keyslist1=self.freq1[sentence[-2]][sentence[-1]].keys()
				valueslist=self.freq1[sentence[-2]][sentence[-1]].values()
				j=j+1
				x=keyslist1[binarysearch.binarysearch(valueslist)]
				sentence.append(x)
		return sentence
	def bigram (self,keyword):
		"""2単語目をランダムに選ぶ"""
		keyslist = self.freq1[keyword].keys()
		y=keyslist[random.randint(0,len(keyslist)-1)]
		return y
