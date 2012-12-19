#!/usr/bin/env python
# -*- coding: utf-8 -*
import sys
import codecs
#メソッド名をsaveinputとかにしたほうがいい？
def saveinput(sentence,dest):
	#これまでの入力をどんどん保存していく
	with codecs.open(dest,'ab','utf-8') as f:
		f.write("".join(sentence))
