#!/usr/bin/env python
# -*- coding: utf-8 -*
import twitterCommunication
import glue
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
	sentence=callSentenceGen.callSentenceGen(reply)
	postTwitter.postTwitter(sentence,reply.user.screen_name)
	previd=reply.id
	filedata1=JsonFile.JsonFile("previd.json")
	filedata1.Write(previd)
