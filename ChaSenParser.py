#!/usr/bin/env python
# -*- coding: utf-8 -*

def ChaSenParser(ChaSenInput):
	lines=ChaSenInput.splitlines()
	parsedlines=[]
	print lines
	for line in lines:
		words=line.split('	')
		parsedlines.append(words)
	return parsedlines
def hinshiStrip(words):
	words.pop()
	words2=[x for x in words if  x[3].find( u'助') == -1 and x[3].find(u'記号') == -1 ]
	return words2
