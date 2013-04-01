
#!/usr/bin/env python
# -*- coding: utf-8 -*
import callSentenceGen
import codecs
import sys
import settingloader

sys.stdout=codecs.getwriter('utf-8')(sys.stdout)
settings=settingloader.loadsettings("settings.json")
argvs=sys.argv
argv=argvs[1]
arg=argv.decode('utf-8')
print arg
reply=arg
if reply !=None:
	modelname=settings["modelname"]
	sentence=callSentenceGen.callSentenceGen_com_pickle(reply,modelname)
	s=" ".join(sentence)
	print s
