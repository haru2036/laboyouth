#!/usr/bin/env python
# -*- coding: utf-8 -*
import unittest
import trigramModelGenerator
class test_trigramModelGenerator(unittest.TestCase):
	def setUp(self):
		self.sentence=u'おはようございます。ボクは元気ですけどなんとか生きてる感じです。最近コーラ飲み過ぎたのか体の調子が悪いです。'
	def test_generateModel_SpaceSaving(self):
		result_default=trigramModelGenerator.generateModel(self.sentence)
		args=self.sentence,10
		result_SS=trigramModelGenerator.generateModel_SpaceSaving(args)
		result_cj2freq=trigramModelGenerator.cjtofreq(result_SS.items())
		print result_default
		print "\n"
		print result_cj2freq
unittest.main()
