#!/usr/bin/env python
# -*- coding: utf-8 -*
import trigramModelGenerator
import keywordext
import codecs
import sentenceGenerator
import cpickler
def callSentenceGen(reply):
	with codecs.open("strarf_serif.txt","rb","utf-8") as f:
		srctxt=[]
		for line in f:
			srctxt.append(line)
			srctxt.append(u"EOS")
	bytesrctxt=" ".join(srctxt)
	freq1=trigramModelGenerator.generateModel(srctxt)
	keyword1=keywordext.extraction(reply.text,freq1)
	sentenceGen=sentenceGenerator.sentenceGenerator(freq1)
	sentence=sentenceGen.generateSentence(keyword1)
	return sentence
def callSentenceGen_com(reply):
	with codecs.open("strarf_serif.txt","rb","utf-8") as f:
	#with codecs.open("Japanese.0304.text.non-mentions.txt","rb","utf-8") as f:
		srctxt=[]
		for line in f:
			srctxt.append(line)
			srctxt.append(u"EOS")
	bytesrctxt=" ".join(srctxt)
	freq1=trigramModelGenerator.generateModel(srctxt)
	cpickler.topickle(freq1)
	keyword1=keywordext.extraction(reply,freq1)
	sentenceGen=sentenceGenerator.sentenceGenerator(freq1)
	sentence=sentenceGen.generateSentence(keyword1)
	return sentence
