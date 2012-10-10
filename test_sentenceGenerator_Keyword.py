#!/usr/bin/env python
# -*- coding: utf-8 -*
import unittest
import sentenceGenerator_Keyword 
class test_sjk(unittest.TestCase):
	def test1(self):
		sjk=sentenceGenerator_Keyword.sjk()
		sjk.main({"inrepid":1234567890})
unittest.main()
