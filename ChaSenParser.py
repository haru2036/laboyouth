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
	#EOSのところが要素が１つだけになっているのでList index out of range エラーが起きる
	words2=[x for x in words if x[3] not in u'助']
	return words2
