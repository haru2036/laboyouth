#!/usr/bin/env python
# -*- coding: utf-8 -*
import sys
import os
import trigramModelGenerator
import mecabCaller
import codecs
import settingloader
argvs=sys.argv
print argvs[-1]
if argvs[-1] is argvs[0] :
	print "最後に学習元ファイル名を指定してください。"
	print "Example:python modelTool.py 'example.txt'"
	sys.exit()
argv=argvs[1]
with codecs.open(argv,"rb","utf-8") as f:
	srctxt=[]
	for line in f:
		srctxt.append(line)
		srctxt.append(u"EOS")
parsedtxt=mecabCaller.parse(srctxt)
settings=settingloader.loadsettings("settings.json")
modelname=settings["modelname"]
modelgen=trigramModelGenerator.modelgenerator()
gen=modelgen.GeneratorForTrigram(parsedtxt)
SS=modelgen.SpaceSaving(gen,settings["k"])
result_cj2freq=modelgen.cjtofreq(SS.items(),modelname)
