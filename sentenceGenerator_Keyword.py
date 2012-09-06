#!/usr/bin/env python
# -*- coding: utf-8 -*
import codecs
import secret
import trigramModelGenerator
import sentenceGenerator
import keywordextr
import sys
import learn
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
		replies=self.api.GetReplies()
		reply_name=replies[0].user.screen_name
		reply_text=replies[0].text
		in_reply_to_id=replies[0].in_reply_to_status_id
		print reply_text
		inputsentence=reply_text.encode('utf-8')
		print in_reply_to_id
		#inputsentence=raw_input()
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
		print sentence
		if not sentence:
			print "sentenceがからです！"
			return
		s= " ".join(sentence)
		poststatus="@"+reply_name+" "+s
		print poststatus
		self.api.PostUpdate(status=poststatus)

