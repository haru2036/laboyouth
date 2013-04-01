#!/usr/bin/env python
# -*- coding: utf-8 -*

import unittest
import keywordextr

class test_keywordextr(unittest.TestCase):
	def testExtraction1(self):
		inputsentence=u'foo bar baz'
		freq1={"foo":{"bar":{"baz":1}}}
		keywordextractor=keywordextr.keywordext(inputsentence,freq1)
		keyword1=keywordextractor.extraction()
		print keyword1
		self.assertIsInstance(keyword1,unicode)
		self.assertEqual(keyword1,"foo")
	def testNone1(self):
		inputsentence=u'hogehoge piyopiyo'
		freq1={"foo":{"bar":{"baz":1}}}
		keywordextractor=keywordextr.keywordext(inputsentence,freq1)
		keyword1=keywordextractor.extraction()
		print keyword1
		self.assertEqual(keyword1,None)
unittest.main()
