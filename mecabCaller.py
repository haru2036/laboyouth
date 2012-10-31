
#!/usr/bin/env python
# -*- coding: utf-8 -*
import MeCab 
class mecabCaller:
	def __init__(self,sentence):
		self.sentence = sentence
	def parse(self):
		itemlist = []
		bytesentence=[]
		bytesentence = [x.encode('utf-8') for x in self.sentence]
		m=MeCab.Tagger("-Owakati")
		for line in bytesentence:
			wakati = m.parse(line)
			wakatistrip=wakati.strip()
			itemlist+=wakatistrip.split(" ")
		itemlist2 = [x.decode('utf-8') for x in itemlist]
		return itemlist2
	def parsekwd(self):
		itemlist=[]
		bytesentence=self.sentence
		print bytesentence
		bytesentence=bytesentence.encode('utf-8')
		m=MeCab.Tagger("-Owakati")
		wakati=m.parse(bytesentence)
		wakatistrip=wakati.strip()
		itemlist+=wakatistrip.split(" ")
		return [x.decode('utf-8') for x in itemlist]
