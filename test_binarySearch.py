#!/usr/bin/env python
# -*- coding: utf-8 -*

import unittest
import binarysearch

class test_binarySearch(unittest.TestCase):
	def testBinSearch1(self):
		weights=1,1
		binSearchResult=binarysearch.binarysearch(weights)
		self.assertLessEqual(binSearchResult,range(2))
unittest.main()
