#!/usr/bin/env python
# -*- coding: utf-8 -*
import mecabCaller
def generateModel(sentence):
	itemlist2=mecabCaller.parse(sentence)
	freq1={}
	for i in xrange(len(itemlist2)-2):
		x=itemlist2[i]
		y=itemlist2[i+1]
		z=itemlist2[i+2]
		if x in freq1:
			if y in freq1[x]:
				if z in freq1[x][y]:
					freq1[x][y][z]+=1
				else:
					freq1[x][y][z]=1
			else:
				freq1[x][y]={z:1}
		else:
			freq2={z:1}
			freq1[x]={y:freq2}
	return freq1
def generateModel_SpaceSaving(sentence,k):
	itemlist2=mecabCaller.parse(sentence)
	cj={}
	for counter in xrange(len(itemlist2)-2):
		x=itemlist2[counter]
		y=itemlist2[counter+1]
		z=itemlist2[counter+2]
		i=x,y,z
		if i in cj:
			cj[i]+=1
		elif len(cj)<k:
			cj[i]=1
		else:
			j=min(cj.values())
			T.append(i)
			T.remove(j)
			
	cPickler.topickle(freq1,"SpaceSaving.dump")
	"""ここに入れ子状の辞書にする処理を書く"""
	pass
