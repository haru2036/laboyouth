
#!/usr/bin/env python
# -*- coding: utf-8 -*
import twitterCommunication
import Inrepid
import getreply
import JsonFile
import callSentenceGen
import postTwitter
import codecs
import sys
import settingloader

sys.stdout=codecs.getwriter('utf-8')(sys.stdout)
settings=settingloader.loadsettings("settings.json")
repid=Inrepid.Inrepid()
reply=getreply.getreply(repid)
if reply !=None:
	modelname=settings["modelname"]
	sentence=callSentenceGen.callSentenceGen_pickle(reply,modelname)
	print sentence
	postTwitter.postTwitter(sentence,reply.user.screen_name,reply.id)
	previd=reply.id
	filedata1=JsonFile.JsonFile("previd.json")
	filedata1.Write(previd)
