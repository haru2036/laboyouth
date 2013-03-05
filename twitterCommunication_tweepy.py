#!/usr/bin/env python
# -*- coding: utf-8 -*
import secret
import tweepy
class twitterCommunication:
	def __init__(self):
		self.auth = tweepy.OAuthHandler(secret.dict['consumer_key'],secret.dict['consumer_secret'])
		self.auth.set_access_token(secret.dict['access_token_key'],secret.dict['access_token_secret'])
		self.api=tweepy.API(self.auth)
	def get(self):
		return self.api.mentions_timeline()
	def post(self,text,inrepid):
		self.api.update_status(text,inrepid)
