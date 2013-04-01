#!/usr/bin/env python
# -*- coding: utf-8 -*
import trigramModelGenerator
import mecabCaller
import keywordext
import codecs
import sentenceGenerator
import cpickler
def callSentenceGen(reply,k):
	with codecs.open("strarf_serif.txt","rb","utf-8") as f:
		srctxt=[]
		for line in f:
			srctxt.append(line)
			srctxt.append(u"EOS")
	modelgen=trigramModelGenerator.modelgenerator()
	gen=modelgen.GeneratorForUnigram(self.itemlist)
	SS=modelgen.SpaceSaving(gen,k)
	freq1=trigramModelGenerator.generateModel(srctxt)
	keyword1=keywordext.extraction(reply.text,freq1)
	sentenceGen=sentenceGenerator.sentenceGenerator(freq1)
	sentence=sentenceGen.generateSentence(keyword1)
	return sentence
def callSentenceGen_com(reply,k):
	#with codecs.open("strarf_serif.txt","rb","utf-8") as f:
	#with codecs.open("Japanese.0304.text.non-mentions.txt","rb","utf-8") as f:
	with codecs.open("strarf_serif.txt","rb","utf-8") as f:
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
def callSentenceGen_com_pickle(reply,modelpath):
	freq1=cpickler.frompickle(modelpath)
	keyword1=keywordext.extraction(reply,freq1)
	sentenceGen=sentenceGenerator.sentenceGenerator(freq1)
	sentence=sentenceGen.generateSentence(keyword1)
	return sentence
def callSentenceGen_pickle(reply,modelpath):
	freq1=cpickler.frompickle(modelpath)
	keyword1=keywordext.extraction(reply.text,freq1)
	sentenceGen=sentenceGenerator.sentenceGenerator(freq1)
	sentence=sentenceGen.generateSentence(keyword1)
	return sentence
