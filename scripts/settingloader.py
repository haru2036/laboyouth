#!/usr/bin/env python
# -*- coding: utf-8 -*
import JsonFile
def loadsettings(filename):
    jsonfile=JsonFile.JsonFile(filename)
    json=jsonfile.Read()
    return json
def writesettings(filename,data):
    jsonfile=JsonFile.JsonFile(filename)
    json=jsonfile.Write(data)
