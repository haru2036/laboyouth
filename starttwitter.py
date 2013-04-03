#!/usr/bin/env python
# -*- coding: utf-8 -*
import scripts.twitterCommunication_tweepy
import scripts.Inrepid
import scripts.getreply
import scripts.JsonFile
import scripts.callSentenceGen
import scripts.postTwitter
import codecs
import sys
import scripts.settingloader

sys.stdout=codecs.getwriter('utf-8')(sys.stdout)
settings=scripts.settingloader.loadsettings("settings.json")
repid=scripts.Inrepid.Inrepid()
reply=scripts.getreply.getreply(repid)
if reply !=None:
	modelname=settings["modelname"]
	sentence=scripts.callSentenceGen.callSentenceGen_pickle(reply,modelname)
	print sentence
	scripts.postTwitter.postTwitter(sentence,reply.user.screen_name,reply.id)
	previd=reply.id
	filedata1=scripts.JsonFile.JsonFile("previd.json")
	filedata1.Write(previd)
elif settings["FromTLTweet"]:
        modelname=settings["modelname"]
	sentence=scripts.callSentenceGen.callSentenceGen_pickle(reply,modelname)
	print sentence
	twitter=scripts.twitterCommunication_tweepy.twitterCommunication(settingloader.loadsettings("secret.json"))
	scripts.postTwitter.postTwitterNormal(sentence,reply.user.screen_name,reply.id)
else:
        sys.exit()
