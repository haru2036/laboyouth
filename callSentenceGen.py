#!/usr/bin/env python
# -*- coding: utf-8 -*
import trigramModelGenerator
import mecabCaller
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
	with codecs.open("strarf_serif.txt","rb","utf-8") as f:
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
	splbyte=[mecabCaller.parse(x) for x in splbyte]
	print len(splbyte),len(splbyte[0]),len(splbyte[1]),len(splbyte[2]),len(splbyte[3])
	args=[(spbyte,k) for spbyte in splbyte]
	p=Pool()
	results=p.map(trigramModelGenerator.generateModel_SpaceSaving,args)
	print "end all process"
	cj=[]
	print "joining results..."
	cj=results[0].copy()
	results.pop(0)
	for result in results:
		cj.update(result)
	print "running cjtofreq..."
	freq1=trigramModelGenerator.cjtofreq(cj.items())
	print freq1
	#cpickler.topickle(freq1,"SpaceSaving.dump")
	keyword1=keywordext.extraction(reply,freq1)
	sentenceGen=sentenceGenerator.sentenceGenerator(freq1)
	sentence=sentenceGen.generateSentence(keyword1)
	return sentence
