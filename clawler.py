#!/usr/bin/env python
# -*- coding: utf-8 -*
import scripts.twitterCommunication_tweepy
import scripts.cpickler
import scripts.settingloader

statuses=scripts.cpickler.frompickle("crawlingtmp.dump")
twitter=scripts.twitterCommunication_tweepy.twitterCommunication(scripts.settingloader.loadsettings("secret.json"))
twitterlist=twitter.getlist("SRCLikebot","Crawlinglist",statuses["newestid"]).timeline()
for item in twitterlist:
    statuses["statuses"].append(item.text)
newestid=twitterlist[0].id
statuses["newestid"]=newestid
scripts.cpickler.topickle(statuses,"crawlingtmp.dump")
