#!/usr/bin/env python
# -*- coding: utf-8 -*
import json

class JsonFile:
	def __init__(self,filepath):
		self.filepath=filepath
	def Read(self):
		with open(self.filepath,'rb') as f:
			return json.load(f)
	def Write(self,contentIn):
		with open(self.filepath,'wb') as f:
			json.dump(contentIn,f)


