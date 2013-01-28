#!/usr/bin/env python
# -*- coding: utf-8 -*
import sys
import codecs
srctxt=[]
with codecs.open("mikatweet.txt","rb","utf-8") as f:
	for line in f:
		linelist=line.split(' ')
		lineinside=[x for x in linelist if u'@' not in x]
		srctxt.append(" ".join(lineinside))
	print srctxt
with codecs.open("mikatweetsp.txt","wb","utf-8") as f:
	f.writelines(srctxt)
