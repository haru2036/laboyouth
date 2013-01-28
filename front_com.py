
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
argvs=sys.argv
argv=argvs[0]
print argv
reply=argv
if reply !=None:
	sentence=callSentenceGen.callSentenceGen(reply)
	print sentence
	previd=reply.id
	filedata1=JsonFile.JsonFile("previd.json")
