#!/usr/bin/env python
# -*- coding: utf-8 -*
import JsonFile
import sys
import codecs
def Inrepid():
	filedata1=JsonFile.JsonFile("previd.json")
	previd = {"inrepid":1234}
	try:
		previd=filedata1.Read()
	except IOError:
		previd["inrepid"]=1234
		filedata1.Write(previd)
	except ValueError:
		previd["inrepid"]=1234
		filedata1.Write(previd)
	return previd
