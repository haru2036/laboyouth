
#!/usr/bin/env python
# -*- coding: utf-8 -*

import mecabCaller
import learn
import random

class keywordext:
	def __init__(self,inputsentence,freq1):
		self.inputsentence=inputsentence
		self.freq=freq1
	def extraction(self):
		itemlist=[]
		learn.learn(self.inputsentence)
		m=mecabCaller.mecabCaller(self.inputsentence)
		itemlist =m.parsekwd() 
		itemlist=[x for x in itemlist if x in self.freq]
		if len(itemlist)==0:
			return None
		keyword1=itemlist[random.randint(0,len(itemlist)-1)]
		print type(keyword1)
		return keyword1
