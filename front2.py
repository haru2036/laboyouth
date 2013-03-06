#!/usr/bin/env python
# -*- coding: utf-8 -*
import twitterCommunication
import secret
import Inrepid
import getreply
import JsonFile
import callSentenceGen
import postTwitter
import codecs
import sys

sys.stdout=codecs.getwriter('utf-8')(sys.stdout)
repid=Inrepid.Inrepid()
reply=getreply.getreply(repid)
if reply !=None:
	sentencelist=[]
	for i in range(0,2):
		sentencelist.append(callSentenceGen.callSentenceGen(reply))
	sentencelist.sort(key=len)
	print sentencelist
	postTwitter.postTwitter(sentencelist[1],reply.user.screen_name,reply.id)
	previd=reply.id
	filedata1=JsonFile.JsonFile("previd.json")
	filedata1.Write(previd)
