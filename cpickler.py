#!/usr/bin/env python
# -*- coding: utf-8 -*
import cPickle
def topickle(importdata):
	with open("pickle.dump","wb") as f:
		cPickle.dump(importdata,f)

