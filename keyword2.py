

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
		itemlist2=[x.decode('utf-8') for x in itemlist]
		keyword1=random.randint(0,len(itemlist2)-1)
		return keyword1
