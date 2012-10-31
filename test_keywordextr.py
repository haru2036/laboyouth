#!/usr/bin/env python
# -*- coding: utf-8 -*

import unittest
import keywordextr

class test_keywordextr(unittest.TestCase):
	def testExtraction1(self):
		inputsentence=u'aiueo kakikukeko sasisuseso tatituteto'
		freq1={'hoge':{'piyo':{'hogehoge',1}}}
		keywordextractor=keywordextr.keywordext(inputsentence,freq1)
		keyword1=keywordextractor.extraction()
		print keyword1
		self.assertIsInstance(keyword1,unicode)
unittest.main()
