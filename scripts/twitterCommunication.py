
#!/usr/bin/env python
# -*- coding: utf-8 -*
import secret
import twitter
class twitterCommunication:
	def __init__(self,secrets):
		self.api = twitter.Api(consumer_key = secrets['consumer_key'],
consumer_secret = secrets['consumer_secret'],
access_token_key = secrets['access_token_key'],
access_token_secret = secrets['access_token_secret'])
	def get(self):
		return self.api.GetReplies()
	def post(self,text):
		self.api.PostUpdate(text)
