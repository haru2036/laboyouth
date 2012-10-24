
#!/usr/bin/env python
# -*- coding: utf-8 -*
import sys
def learn(sentence):
	f=open('learn.txt','a')
	try:
		f.write(sentence.encode('utf-8'))
	finally:
		f.close()
