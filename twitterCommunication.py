
#!/usr/bin/env python
# -*- coding: utf-8 -*
import secret
import twitter
class twitterCommunication:
	def __init__(self):
		self.api = twitter.Api(consumer_key = secret.dict['consumer_key'],
consumer_secret = secret.dict['consumer_secret'],
access_token_key = secret.dict['access_token_key'],
access_token_secret = secret.dict['access_token_secret'])
	def get(self):
		return self.api.GetReplies()
	def post(self,text):
		self.api.PostUpdate(text)
