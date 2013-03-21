#!/usr/bin/env python
# -*- coding: utf-8 -*
import mecabCaller
import cpickler
def generateModel(sentence):
	print sentence
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
def generateModel_SpaceSaving(args):
	sentence,k=args
	itemlist2=mecabCaller.parse(sentence)
	print "job.start()"
	print "generating..."
	cj={}
	x=itemlist2[0]
	y=itemlist2[1]
	z=itemlist2[2]
	buckets={}
	minimum=0
	for counter in xrange(len(itemlist2)-2):
		z=itemlist2[counter+2]
		i=x,y,z
		if i in cj:
			cj[i]+=1
			if i in buckets[minimum]:
				buckets[minimum].remove(i)
				buckets[minimum+1].append(i)
			if len(buckets[minimum]) is 0:
				minimum+=1
				buckets[minimum].pop()
		elif len(cj)<k:
			cj[i]=1
			if buckets.get(1) is None:
				buckets[1]=[i]
			else:
				buckets[1].append(i)
			minimum=1
		else:
			j=buckets[minimum].pop()
			cj[i]=cj[j]+1
			if buckets.get(cj[j]+1) is None:
				buckets.setdefault(cj[j]+1,[i])
			else:
				buckets[cj[j]+1].append(i)
			del(cj[j])
			if len(buckets[minimum]) is 0:
				del buckets[minimum]
				minimum=min(buckets.keys())
		x=y
		y=z
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
