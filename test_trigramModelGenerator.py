#!/usr/bin/env python
# -*- coding: utf-8 -*
import unittest
from datetime import datetime
import trigramModelGenerator
import codecs
class test_trigramModelGenerator(unittest.TestCase):
	def setUp(self):
		self.sentence=[]
		self.itemlist=["A","B","C","C","D","A","B","B","A","D","C","B","C","A","D","A","C","D","B","D","A","A","D"]
		with codecs.open("strarf_serif.txt",'rb','utf-8') as f:
			for line in f:
				self.sentence.append(line)
				self.sentence.append(u"EOS")
	def test_generateModel_SpaceSaving(self):
		time_start=datetime.now()
		result_default=trigramModelGenerator.generateModel(self.sentence)
		time_defaultEnded=datetime.now()
		args=self.sentence,10000
		result_SS=trigramModelGenerator.generateModel_SpaceSaving(args)
		result_cj2freq=trigramModelGenerator.cjtofreq(result_SS.items())
		time_SSEnded=datetime.now()
		print time_start,time_defaultEnded,time_SSEnded
		time_default=time_defaultEnded - time_start
		time_SS=time_SSEnded - time_defaultEnded
		print 'Default,SS'
		print time_default,time_SS
		print result_cj2freq
	def test_generateModel_SpaceSavingUsingGenerator(self):
		args=self.itemlist,3
		SS=trigramModelGenerator.generateModel_SpaceSaving_Unigram(args)
		self.assertEqual(SS,{"A":8,"B":7,"D":8})
unittest.main()
