#!/usr/bin/env python
# -*- coding: utf-8 -*
import mecabCaller
import cpickler
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
	print freq1
	return freq1
def generateModel_SpaceSaving(args):
	itemlist2,k=args
	print "job.start()"
	print "generating..."
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
			#とりあえず真似してみる
			j=min(cj,key=lambda x:cj[x])
			cj[i]=cj[j]+1
			del(cj[j])
	print "end of generate"
	return cj
def cjtofreq(cj):
	freq1={}
	for j in cj:
		x=j[0][0]
		y=j[0][1]
		z=j[0][2]
		ci=j[1]
		if x in freq1:
			if y in freq1[x]:
				if z in freq1[x][y]:
					freq1[x][y][z]+=1
				else:
					freq1[x][y][z]=ci
			else:
				freq1[x][y]={z:ci}
		else:
			freq1[x]={y:{z:ci}}
	#freq1[i[0][0]][i[0][1]][i[0][2]]=i[1]
	cpickler.topickle(freq1,"SpaceSaving.dump")
	return freq1
