#!/usr/bin/env python
# -*- coding: utf-8 -*
import twitterCommunication_tweepy

def postTwitter(sentence,reply_name):
	twitter=twitterCommunication_tweepy.twitterCommunication()
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
