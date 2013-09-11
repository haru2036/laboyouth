#!/usr/bin/env python
# -*- coding: utf-8 -*
import keywordext
import sentenceGenerator
import cpickler

class callSentenceGenClass:
	def __init__(self,modelpath):
		self.freq1=cpickler.frompickle(modelpath)
	def callSentenceGen_pickle(self,reply):
		keyword1=keywordext.extraction(reply,self.freq1)
		sentenceGen=sentenceGenerator.sentenceGenerator(self.freq1)
		sentence=sentenceGen.generateSentence(keyword1)
		return sentence
