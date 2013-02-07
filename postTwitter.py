#!/usr/bin/env python
# -*- coding: utf-8 -*
import twitterCommunication_tweepy

def postTwitter(sentence,reply_name,inrepid):
	twitter=twitterCommunication_tweepy.twitterCommunication()
	if not sentence:
		print "sentenceが空です。"
		return
	if sentence==None:
		print "sentence[0]がNoneです。"
		return
	s= "".join(sentence)
	poststatus_long="@"+reply_name+" "+s
	poststatus=poststatus_long[:140]
	print len(poststatus)
	twitter.post(poststatus,inrepid)
