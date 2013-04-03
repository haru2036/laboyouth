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
	def get_mainTL(self):
                return self.api.home_timeline()
	def post(self,text,inrepid):
		self.api.update_status(text,inrepid)
	def postnormal(self,text):
		self.api.update_status(text)
	def getlists(self):
                return self.api.lists_all()
        def getlist(self,owner,slug,sinceid):
                return self.api.get_list(since_id=sinceid,owner_screen_name=owner,slug=slug)
