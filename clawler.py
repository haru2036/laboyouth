#!/usr/bin/env python
# -*- coding: utf-8 -*
import scripts.twitterCommunication_tweepy
import scripts.cpickler
import scripts.settingloader
import sys

settings=scripts.settingloader.loadsettings("settings.json")
if settings["executingNum"] != 0:
    sys.exit()
    pass
try:
    statuses=scripts.cpickler.frompickle("crawlingtmp.dump")
except IOError:
    statuses=scripts.cpickler.frompickle("initcrawlingtmp.dump")
twitter=scripts.twitterCommunication_tweepy.twitterCommunication(scripts.settingloader.loadsettings("secret.json"))
twitterlist=twitter.getlist("SRCLikebot","Crawlinglist",statuses["newestid"])
for item in twitterlist:
    statuses["statuses"].append(item.text)
newestid=twitterlist[0].id
statuses["newestid"]=newestid
scripts.cpickler.topickle(statuses,"crawlingtmp.dump")
