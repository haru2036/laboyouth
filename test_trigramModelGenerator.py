#!/usr/bin/env python
# -*- coding: utf-8 -*
import unittest
from datetime import datetime
import trigramModelGenerator
class test_trigramModelGenerator(unittest.TestCase):
	def setUp(self):
		self.sentence=u'おはようございます。ボクは元気ですけどなんとか生きてる感じです。最近コーラ飲み過ぎたのか体の調子が悪いです。'
	def test_generateModel_SpaceSaving(self):
		time_start=datetime.now()
		result_default=trigramModelGenerator.generateModel(self.sentence)
		time_defaultEnded=datetime.now()
		args=self.sentence,10
		result_SS=trigramModelGenerator.generateModel_SpaceSaving(args)
		result_cj2freq=trigramModelGenerator.cjtofreq(result_SS.items())
		time_SSEnded=datetime.now()
		print time_start,time_defaultEnded,time_SSEnded
		print time_defaultEnded - time_start,time_SSEnded - time_defaultEnded
unittest.main()
