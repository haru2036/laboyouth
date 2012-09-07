#!/usr/bin/env python
# -*- coding: utf-8 -*
import json

class fileRW:
	def __init__(self,filepath):
		self.filepath=filepath
	def fileR(self):
		f=open(self.filepath)
		content=json.load(f)
		f.close()
		return content
	def fileW(self,contentIn):
		f=open(self.filepath,"w")
		self.contentIn=contentIn
		json.dump(self.contentIn,f)
		f.close()


