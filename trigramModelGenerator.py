#!/usr/bin/env python
# -*- coding: utf-8 -*
import cpickler
class modelgenerator():
	def __init__(self):
		self.itemlist2=[]
		self.cj={}
		self.buckets={}
		self.minimum=0
	def nativecounting(self,gen):
		for i in gen:
			if i in self.cj:
				self.cj[i]+=1
			else:
				self.cj[1]=1
		return self.cj
	def SpaceSaving(self,gen,k):
		for i in gen:
			if i in self.cj:
				if i in self.buckets[self.minimum]:
					self.buckets[self.minimum].remove(i)
					if self.buckets.get(self.minimum+1) is None:
						self.buckets[self.minimum+1]=[i]
					else:
						self.buckets[self.minimum+1].append(i)
				else:
					self.buckets[self.cj[i]].remove(i)
					if self.buckets.get(self.cj[i]+1) is None:
						self.buckets[self.cj[i]+1]=[i]
					else:
						self.buckets[self.cj[i]+1].append(i)
				self.cj[i]+=1
				if len(self.buckets[self.minimum]) is 0:
					del self.buckets[self.minimum]
					self.minimum+=1
				elif len(self.buckets[self.cj[i]-1]) is 0:
					del self.buckets[self.cj[i]-1] 
				print "ended if"
				print self.buckets
			elif len(self.cj)<k:
				self.cj[i]=1
				if self.buckets.get(1) is None:
					self.buckets[1]=[i]
				else:
					self.buckets[1].append(i)
				self.minimum=1
				print "ended elif"
				print self.buckets
			else:
				if len(self.buckets[self.minimum]) is 0:
					del self.buckets[self.minimum]
					self.minimum=min(self.buckets.keys())
				j=self.buckets[self.minimum].pop()
				self.cj[i]=self.cj[j]+1
				if self.buckets.get(self.cj[j]+1) is None:
					self.buckets.setdefault(self.cj[j]+1,[i])
				else:
					self.buckets[self.cj[j]+1].append(i)
				del(self.cj[j])
				print "ended else"
				print self.buckets
		return self.cj
	def GeneratorForUnigram(self,itemlist2):
		for i in itemlist2:
			yield i
	def GeneratorForTrigram(self,itemlist2):
		x=itemlist2[0]
		y=itemlist2[1]
		z=itemlist2[2]
		for counter in xrange(len(itemlist2)-2):
			z=itemlist2[counter+2]
			i=x,y,z
			yield i
			x=y
			y=z
	def cjtofreq(self,cj):
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
