#!/usr/bin/env python
# -*- coding: utf-8 -*
import codecs
import json
import secret
import trigramModelGenerator
import sentenceGenerator
import keywordext
import sys
import learn
import fileRW
class glue:
	def __init__(self,twitterCommunication):
		self.twitter = twitterCommunication
	def main(self):
		filedata1=fileRW.fileRW("previd.json")
		previd = {"inrepid":1234}
		sys.stdout=codecs.getwriter('utf-8')(sys.stdout)
		srctxt=[]
		try:
			previd=filedata1.fileR()
		except IOError:
			previd["inrepid"]=1234
			filedata1.fileW(previd)
		except ValueError:
			previd["inrepid"]=1234
			filedata1.fileW(previd)
		replies = self.twitter.get()
		print replies[0]
		reply_name=replies[0].user.screen_name
		reply_text=replies[0].text
		in_reply_to_id=replies[0].id
		print reply_text
		inputsentence=reply_text
		print in_reply_to_id
		if previd["inrepid"]==in_reply_to_id:
			print u"すでに最新のツイートに返信しています。"
			return
		previd["inrepid"]=in_reply_to_id
		with codecs.open("strarf_serif.txt","rb","utf-8") as f:
			for line in f:
				srctxt.append(line)
		bytesrctxt=" ".join(srctxt)
		modelGen=trigramModelGenerator.trigramModelGenerator(srctxt)
		freq1=modelGen.generateModel()
		keyword1=keywordext.extraction(inputsentence,freq1)
		filedata1.fileW(previd)
		sentenceGen=sentenceGenerator.sentenceGenerator(freq1)
		sentence=sentenceGen.generateSentence(keyword1)
		print sentence
		if not sentence:
			print "sentenceが空です。"
			return
		if sentence==None:
			print "sentence[0]がNoneです。"
			return
		s= " ".join(sentence)
		poststatus="@"+reply_name+" "+s
		print poststatus
		self.twitter.post(poststatus)
