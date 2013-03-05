#!/usr/bin/env python
# -*- coding: utf-8 -*
import codecs
with codecs.open("Japanese.0304.txt","rb","utf-8") as f:
	srctxt=[]
	for line in f:
		srctxt.append(line.split("	"))
textlist=[x[-1] for x in srctxt]
with codecs.open("Japanese.0304.text.txt","wb","utf-8") as f:
	f.write("".join(textlist))
