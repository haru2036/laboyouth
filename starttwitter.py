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
	sentencelist=[]
	for i in range(0,2):
		sentencelist.append(scripts.callSentenceGen.callSentenceGen_pickle(reply,modelname))
	print sentencelist
	sentencelist.sort(key=len)
	scripts.postTwitter.postTwitter(sentencelist[1],reply.user.screen_name,reply.id)
	previd=reply.id
	filedata1=scripts.JsonFile.JsonFile("previd.json")
	filedata1.Write(previd)
elif settings["FromTLTweet"]:
        modelname=settings["modelname"]
        twitter=scripts.twitterCommunication_tweepy.twitterCommunication(scripts.settingloader.loadsettings("secret.json"))
	TL=twitter.get_mainTL()
	tweet=TL[0]
	sentencelist=[]
	for i in range(0,2):
                sentencelist.append(scripts.callSentenceGen.callSentenceGen_pickle(tweet,modelname))
	sentencelist.sort(key=len)
	print sentencelist
	scripts.postTwitter.postTwitterNormal(sentencelist[1])
else:
        sys.exit()
