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
	cpickler.topickle(freq1,"plaincounting.dump")
	return freq1
def SSgen(sentence):
	itemlist2=mecabCaller.parse(sentence)
	print "job.start()"
	print "generating..."
	x=itemlist2[0]
	y=itemlist2[1]
	z=itemlist2[2]
	buckets={}
	minimum=0
	for counter in xrange(len(itemlist2)-2):
		z=itemlist2[counter+2]
		i=x,y,z
		yield i
		x=y
		y=z
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
def generateModel_SpaceSaving_Unigram(args):
	itemlist2,k=args
	cj={}
	buckets={}
	for i in itemlist2:
		if i in cj:
			if i in buckets[minimum]:
				buckets[minimum].remove(i)
				if buckets.get(minimum+1) is None:
					buckets[minimum+1]=[i]
				else:
					buckets[minimum+1].append(i)
			else:
				buckets[cj[i]].remove(i)
				if buckets.get(cj[i]+1) is None:
					buckets[cj[i]+1]=[i]
				else:
					buckets[cj[i]+1].append(i)
			cj[i]+=1
			if len(buckets[minimum]) is 0:
				del buckets[minimum]
				minimum+=1
		elif len(cj)<k:
			cj[i]=1
			if buckets.get(1) is None:
				buckets[1]=[i]
			else:
				buckets[1].append(i)
			minimum=1
		else:
			if len(buckets[minimum]) is 0:
				del buckets[minimum]
				minimum=min(buckets.keys())
			j=buckets[minimum].pop()
			cj[i]=cj[j]+1
			if buckets.get(cj[j]+1) is None:
				buckets.setdefault(cj[j]+1,[i])
			else:
				buckets[cj[j]+1].append(i)
			del(cj[j])
	return cj
def generateModel_SpaceSaving(args):
	itemlist2,k=args
	gen=SSgen(itemlist2)
	cj={}
	buckets={}
	for i in gen:
		if i in cj:
			if i in buckets[minimum]:
				buckets[minimum].remove(i)
				if buckets.get(minimum+1) is None:
					buckets[minimum+1]=[i]
				else:
					buckets[minimum+1].append(i)
			else:
				buckets[cj[i]].remove(i)
				if buckets.get(cj[i]+1) is None:
					buckets[cj[i]+1]=[i]
				else:
					buckets[cj[i]+1].append(i)
			cj[i]+=1
			if len(buckets[minimum]) is 0:
				del buckets[minimum]
				minimum+=1
		elif len(cj)<k:
			cj[i]=1
			if buckets.get(1) is None:
				buckets[1]=[i]
			else:
				buckets[1].append(i)
			minimum=1
		else:
			if len(buckets[minimum]) is 0:
				del buckets[minimum]
				minimum=min(buckets.keys())
			j=buckets[minimum].pop()
			cj[i]=cj[j]+1
			if buckets.get(cj[j]+1) is None:
				buckets.setdefault(cj[j]+1,[i])
			else:
				buckets[cj[j]+1].append(i)
			del(cj[j])
	return cj
