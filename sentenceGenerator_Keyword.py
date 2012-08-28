#!/usr/bin/env python
# -*- coding: utf-8 -*
import codecs
import secret
import trigramModelGenerator
import sentenceGenerator
import keywordextr
import sys
import twitter
class sjk:

	def __init__(self):
		self.api = twitter.Api(consumer_key = secret.dict['consumer_key'],consumer_secret = secret.dict['consumer_secret'],access_token_key = secret.dict['access_token_key'],access_token_secret = secret.dict['access_token_secret']
			)
	def main(self):
#文字コード設定
		sys.stdout=codecs.getwriter('utf_8')(sys.stdout)
		srctxt=[]
		print u"こんにちは！"
#keyword="こんにちは"
		inputsentence=raw_input()
		extkey=keywordextr.keywordext(inputsentence)
		keyword1=extkey.extraction()
#with open("strarf_serif.txt","rb") as f:
		with open("strarf_serif.txt","rb") as f:
			for line in f:
				srctxt.append(line)
		modelGen=trigramModelGenerator.trigramModelGenerator(srctxt)
		freq1=modelGen.generateModel()
		sentenceGen=sentenceGenerator.sentenceGenerator(freq1,keyword1)
		sentence=sentenceGen.generateSentence()
		s= u" ".join(sentence)
		print s
		self.api.PostUpdate(status=s)

