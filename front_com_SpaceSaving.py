#!/usr/bin/env python
# -*- coding: utf-8 -*
import callSentenceGen
import codecs
import sys

sys.stdout=codecs.getwriter('utf-8')(sys.stdout)
argvs=sys.argv
argv=argvs[1]
arg=argv.decode('utf-8')
print arg
reply=arg
if reply !=None:
	sentence=callSentenceGen.callsentencegen_com_SpaceSaving(reply)
	s=" ".join(sentence)
	print s
