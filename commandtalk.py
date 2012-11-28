#!/usr/bin/env python
# -*- coding: utf-8 -*
import codecs
import json
import secret
import trigramModelGenerator
import sentenceGenerator
import keywordextr
import sys
import learn
import fileRW
sys.stdout=codecs.getwriter('utf-8')(sys.stdout)
with codecs.open("strarf_serif.txt","rb","utf-8")as f:
	for line in f:
		srctxt.append(line)
bytesrctxt=" ".join(srfctxt)
modelGen=trigramModelGenerator.trigramModelGenerator(srctxt)
freq1=modelGen.generateModel()
extkey=keywordextr.keywordext(inputsentence,freq1)
keyword1=extkey.extraction()
sentenceGen=sentenceGenerator.sentenceGenerator(freq1,keyword1)
sentence=sentenceGen.generateSentence()
print sentence
if not sentence:
	print "sentenceが空です。"
	return
if sentence==None:
	print "sentence[0]がNoneです。"
	return
s=" ".join(sentence)
print s

