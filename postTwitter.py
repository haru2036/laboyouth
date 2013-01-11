#!/usr/bin/env python
# -*- coding: utf-8 -*
import twitterCommunication

def postTwitter(sentence,reply_name):
	twitter=twitterCommunication.twitterCommunication()
	if not sentence:
		print "sentenceが空です。"
		return
	if sentence==None:
		print "sentence[0]がNoneです。"
		return
	s= " ".join(sentence)
	s=s.strip(" ")
	poststatus="@"+reply_name+" "+s
	print poststatus
	twitter.post(poststatus)
