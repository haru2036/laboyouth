#!/usr/bin/env python
# -*- coding: utf-8 -*
import sys
import codecs
srctxt=[]
with codecs.open("strarf_serif.txt","rb","utf-8") as f:
	for line in f:
		lineinside=line.strip(u'「」')
		srctxt.append("".join(lineinside))
	print srctxt
with codecs.open("strarf_serif_sp.txt","wb","utf-8") as f:
	f.writelines(srctxt)
