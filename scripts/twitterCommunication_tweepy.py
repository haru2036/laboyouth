#!/usr/bin/env python
# -*- coding: utf-8 -*
import tweepy
class twitterCommunication:
	def __init__(self,secret):
		self.auth = tweepy.OAuthHandler(secret['consumer_key'],secret['consumer_secret'])
		self.auth.set_access_token(secret['access_token_key'],secret['access_token_secret'])
		self.api=tweepy.API(self.auth)
	def get(self):
		return self.api.mentions_timeline()
	def post(self,text,inrepid):
		self.api.update_status(text,inrepid)
