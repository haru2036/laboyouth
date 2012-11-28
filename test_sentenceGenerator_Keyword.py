#!/usr/bin/env python
# -*- coding: utf-8 -*
import unittest
import sentenceGenerator_Keyword 
class test_sjk(unittest.TestCase):
	def inreptest(self):
		sjk=sentenceGenerator_Keyword.sjk()
		sjk.main()
		assert
	def test_splittest(self):
		sjk=sentenceGenerator_Keyword.sjk()
		sjk.main({"inrepid":1234567890})
unittest.main()
