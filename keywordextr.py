

import MeCab
import learn
import random

class keywordext:
	def __init__(self,inputsentence):
		self.inputsentence=inputsentence
	def extraction(self):
		itemlist=[]
		learn.learn(self.inputsentence)
		inputlist=self.inputsentence.split(" ")
		m=MeCab.Tagger("-Owakati")
		wakati=m.parse(inputlist[1])
		wakatistrip=wakati.strip()
		itemlist+=wakatistrip.split(" ")
		keyword1=itemlist[random.randint(0,len(itemlist)-1)]
		return keyword1
