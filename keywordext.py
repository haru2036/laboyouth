#!/usr/bin/env python
# -*- coding: utf-8 -*

import mecabCaller
import random
def extraction(inputsentence,freq1):
	#ここには入力文を保存するメソッドの呼び出しがあったもののここにはふさわしくないような気がしたので撤去
	rawitemlist =mecabCaller.parsekeywordChasen(inputsentence)
	itemlist=[x[2] for x in rawitemlist]
	print itemlist
	itemlist=[x for x in itemlist if x in freq1]
	if len(itemlist)==0:
		return None
	print itemlist
	keyword1=itemlist[random.randint(0,len(itemlist)-1)]
	print type(keyword1)
	return keyword1
