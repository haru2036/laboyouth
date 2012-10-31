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
import twitter
import fileRW
class sjk:
	def __init__(self):
		self.api = twitter.Api(consumer_key = secret.dict['consumer_key'],consumer_secret = secret.dict['consumer_secret'],access_token_key = secret.dict['access_token_key'],access_token_secret = secret.dict['access_token_secret']
			)
	def main(self):
#文字コード設定
		filedata1=fileRW.fileRW("previd.json")
		previd={"inrepid":1234}
		sys.stdout=codecs.getwriter('utf_8')(sys.stdout)
		srctxt=[]
		print u"こんにちは！"
#keyword="こんにちは"
		try:
			previd=filedata1.fileR()
		except IOError:
			previd["inrepid"]=1234
			filedata1.fileW(previd)
		except ValueError:
			previd["inrepid"]=1234
			filedata1.fileW(previd)
		replies=self.api.GetReplies()
		print replies[0]
		reply_name=replies[0].user.screen_name
		reply_text=replies[0].text
		in_reply_to_id=replies[0].id
		print reply_text
		inputsentence=reply_text
		print in_reply_to_id
		inputsentence=inputsentence.split('@')
		if previd["inrepid"]==in_reply_to_id:
			print u"すでに返信済みのツイートが最新です。"
			return
		previd["inrepid"]=in_reply_to_id
		#inputsentence=raw_input()
		with open("strarf_serif.txt","rb") as f:
			for line in f:
				srctxt.append(line)
		modelGen=trigramModelGenerator.trigramModelGenerator(srctxt)
		freq1=modelGen.generateModel()
		extkey=keywordextr.keywordext(inputsentence,freq1)
		keyword1=extkey.extraction()
		filedata1.fileW(previd)
		sentenceGen=sentenceGenerator.sentenceGenerator(freq1,keyword1)
		sentence=sentenceGen.generateSentence()
		print sentence
		if not sentence:
			print "sentenceがからです！"
			return
		s= " ".join(sentence)
		poststatus="@"+reply_name+" "+s
		print poststatus
		self.api.PostUpdate(status=poststatus)

