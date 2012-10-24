
#!/usr/bin/env python
# -*- coding: utf-8 -*

import mecabCaller
import learn
import random

class keywordext:
	def __init__(self,inputsentence):
		self.inputsentence=inputsentence
	def extraction(self):
		itemlist=[]
		learn.learn(self.inputsentence)
		m=mecabCaller.mecabCaller(self.inputsentence)
		itemlist =m.parsekwd() 
		keyword1=itemlist[random.randint(0,len(itemlist)-1)]
		print type(keyword1)
		return keyword1
