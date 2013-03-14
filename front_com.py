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
argvs=sys.argv
argv=argvs[1]
arg=argv.decode('utf-8')
print arg
reply=arg
if reply !=None:
	sentence=callSentenceGen.callSentenceGen_com(reply)
	s=" ".join(sentence)
	print s
