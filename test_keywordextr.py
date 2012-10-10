#!/usr/bin/env python
# -*- coding: utf-8 -*

import unittest
import keywordextr

class test_keywordextr(unittest.TestCase):
	def testExtraction1(self):
		inputsentence=u"こんにちは、私は元気です。あなたは元気ですか？"
		keywordextractor=keywordextr.keywordext(inputsentence)
		keyword1=keywordextractor.extraction()
		print keyword1
		self.assertIsInstance(keyword1,unicode)
unittest.main()
