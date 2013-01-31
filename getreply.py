#!/usr/bin/env python
# -*- coding: utf-8 -*
import twitterCommunication_tweepy 

def getreply(inrepid):
	twitter=twitterCommunication_tweepy.twitterCommunication()
	replies=twitter.get()
	print replies[0]
	in_reply_to_id=replies[0].id
	inputsentence=replies[0].text
	if inrepid==in_reply_to_id:
		print u"すでに最新のツイートに返信しています。"
		return
	return replies[0]
