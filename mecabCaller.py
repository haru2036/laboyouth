#!/usr/bin/env python
# -*- coding: utf-8 -*
import MeCab 
def parse(sentence):
	itemlist = []
	bytesentence=[]
	bytesentence = [x.encode('utf-8') for x in sentence]
	m=MeCab.Tagger("-Owakati")
	for line in bytesentence:
		wakati = m.parse(line).decode('utf-8')
		wakatistrip=wakati.strip()
		itemlist+=wakatistrip.split(" ")
	"""itemlist2 = [x.decode('utf-8') for x in itemlist]
	return itemlist2
	"""
	return itemlist
def parsekeyword(sentence):
	itemlist=[]
	bytesentence=sentence
	print bytesentence
	bytesentence=bytesentence.encode('utf-8')
	m=MeCab.Tagger("-Owakati")
	wakati=m.parse(bytesentence).decode('utf-8')
	wakatistrip=wakati.strip()
	itemlist+=wakatistrip.split(" ")
	#return [x.decode('utf-8') for x in itemlist]
	return itemlist
