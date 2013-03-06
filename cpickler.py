#!/usr/bin/env python
# -*- coding: utf-8 -*
import cPickle
def topickle(importdata):
	with open("pickle.sampleapitweets.dump","wb") as f:
		cPickle.dump(importdata,f)
def frompickle(filename):
	with open(filename,"rb") as f:
		return cPickle.load(f)
