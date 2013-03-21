#!/usr/bin/env python
# -*- coding: utf-8 -*
import unittest
from datetime import datetime
import trigramModelGenerator
import codecs
class test_trigramModelGenerator(unittest.TestCase):
	def setUp(self):
		srctxt=[]
		with codecs.open("xaa",'rb','utf-8') as f:
			for line in f:
				srctxt.append(line)
				srctxt.append(u"EOS")
		self.sentence=" ".join(srctxt)
	def test_generateModel_SpaceSaving(self):
		time_start=datetime.now()
		result_default=trigramModelGenerator.generateModel(self.sentence)
		time_defaultEnded=datetime.now()
		args=self.sentence,1000
		result_SS=trigramModelGenerator.generateModel_SpaceSaving(args)
		result_cj2freq=trigramModelGenerator.cjtofreq(result_SS.items())
		time_SSEnded=datetime.now()
		print time_start,time_defaultEnded,time_SSEnded
		time_default=time_defaultEnded - time_start
		time_SS=time_SSEnded - time_defaultEnded
		print 'Default,SS'
		print time_default,time_SS
		print time_default//time_SS,"%"
unittest.main()
