

import MeCab
import random

class keywordext:
	def __init__(self,inputsentence):
		self.inputsentence=inputsentence
	def extraction(self):
		itemlist=[]
		m=MeCab.Tagger("-Owakati")
		wakati=m.parse(self.inputsentence)
		wakatistrip=wakati.strip()
		itemlist+=wakatistrip.split(" ")
		keyword1=itemlist[random.randint(0,len(itemlist)-1)]
		return keyword1
