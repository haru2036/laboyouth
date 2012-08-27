#!/usr/bin/env python
# -*- coding: utf-8 -*
import codecs
import trigramModelGenerator
import sentenceGenerator
import sys
#文字コード設定
sys.stdout=codecs.getwriter('utf_8')(sys.stdout)
srctxt=[]
print u"こんにちは！"
#keyword="こんにちは"
keyword=raw_input()
#with open("strarf_serif.txt","rb") as f:
with open("strarf_serif.txt","rb") as f:
	for line in f:
		srctxt.append(line)
modelGen=trigramModelGenerator.trigramModelGenerator(srctxt)
freq1=modelGen.generateModel()
sentenceGen=sentenceGenerator.sentenceGenerator(freq1,keyword)
sentence=sentenceGen.generateSentence()
print u" ".join(sentence)
