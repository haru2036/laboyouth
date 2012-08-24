#!/usr/bin/env python
# -*- coding: utf-8 -*
import codecs
import trigramGenerator
import sys
#文字コード設定
sys.stdout=codecs.getwriter('utf_8')(sys.stdout)
srctxt=[]
print u"こんにちは！"
keyword=raw_input()
with open("strarf_serif.txt","rb") as f:
	for line in f:
		srctxt.append(line)
sentence=trigramGenerator.trigramGenerator(keyword,srctxt)
print u" ".join(sentence)
