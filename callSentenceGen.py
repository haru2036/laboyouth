#!/usr/bin/env python
# -*- coding: utf-8 -*
import trigramModelGenerator
import keywordext
import codecs
import sentenceGenerator
import cpickler
from multiprocessing import Process,Queue,Pool 
def callSentenceGen(reply):
	with codecs.open("strarf_serif.txt","rb","utf-8") as f:
		srctxt=[]
		for line in f:
			srctxt.append(line)
			srctxt.append(u"EOS")
	bytesrctxt=" ".join(srctxt)
	freq1=trigramModelGenerator.generateModel(srctxt)
	keyword1=keywordext.extraction(reply.text,freq1)
	sentenceGen=sentenceGenerator.sentenceGenerator(freq1)
	sentence=sentenceGen.generateSentence(keyword1)
	return sentence
def callSentenceGen_com(reply):
	#with codecs.open("strarf_serif.txt","rb","utf-8") as f:
	#with codecs.open("Japanese.0304.text.non-mentions.txt","rb","utf-8") as f:
	with codecs.open("strarf_serif.txt","rb","utf-8") as f:
		srctxt=[]
		for line in f:
			srctxt.append(line)
			srctxt.append(u"EOS")
	bytesrctxt=" ".join(srctxt)
	freq1=trigramModelGenerator.generateModel(srctxt)
	cpickler.topickle(freq1)
	keyword1=keywordext.extraction(reply,freq1)
	sentenceGen=sentenceGenerator.sentenceGenerator(freq1)
	sentence=sentenceGen.generateSentence(keyword1)
	return sentence
def callSentenceGen_pickle(reply):
	freq1=cpickler.frompickle("SpaceSaving.dump")
	keyword1=keywordext.extraction(reply,freq1)
	sentenceGen=sentenceGenerator.sentenceGenerator(freq1)
	sentence=sentenceGen.generateSentence(keyword1)
	return sentence
def callsentencegen_com_SpaceSaving(reply):
	#with codecs.open("strarf_serif.txt","rb","utf-8") as f:
	#with codecs.open(Japanese.0304.text.non-mentions.txt","rb","utf-8") as f:
	with codecs.open("xaa","rb","utf-8") as f:
		srctxt=[]
		for line in f:
			srctxt.append(line)
			srctxt.append(u"EOS")
	bytesrctxt=" ".join(srctxt)
	k=10000
	length=len(bytesrctxt)
	spcount=4
	splen=length/spcount
	print splen
	splbyte=[bytesrctxt[:splen]]
	for i in xrange(0,spcount-1):
		splbyte.append(bytesrctxt[splen*i:splen*i+splen])
	#splbyte=[bytesrctxt[i:i+size] for i in range(0,len(bytesrctxt),size)]
	print len(splbyte),len(splbyte[0]),len(splbyte[1]),len(splbyte[2]),len(splbyte[3])
	
	result_queue=Queue()
	jobs=[Process(target=trigramModelGenerator.generateModel_SpaceSaving,args=(result_queue,bytetexts,k)) for bytetexts in splbyte]
	for job in jobs:job.start()
	for job in jobs:job.join()
	print "end all process"
	results=[result_queue.get() for ss in jobs]
	cj=[]
	results=[x.items() for x in results]
	print "joining results..."
	for result in results:
		cj=[x for sublist in [cj,result] for x in sublist]
	"""
	p=Pool()
	argtuple=(bytesrctxt,40000)
	print type(argtuple)
	cj=p.map(trigramModelGenerator.generateModel_SpaceSaving,argtuple)
	"""
	print "running cjtofreq..."
	freq1=trigramModelGenerator.cjtofreq(cj)
	#cpickler.topickle(freq1,"SpaceSaving.dump")
	keyword1=keywordext.extraction(reply,freq1)
	sentenceGen=sentenceGenerator.sentenceGenerator(freq1)
	sentence=sentenceGen.generateSentence(keyword1)
	return sentence
