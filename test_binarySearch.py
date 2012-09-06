#!/usr/bin/env python
# -*- coding: utf-8 -*

import unittest
import binarysearch
#前提の仕様
#Randomも出力も0からlen(weights)-1の範囲のみ。
#それ以外が出てきたらおかしいということになる。
class test_binarySearch(unittest.TestCase):
	def testBinSearch1(self):
		weights=1,1
		binSearchResult=binarysearch.binarysearch(weights,0)
		self.assertEqual(binSearchResult,0)
		binSearchResult=binarysearch.binarysearch(weights,1)
		self.assertEqual(binSearchResult,1)
		#binSearchResult=binarysearch.binarysearch(weights,2)
		#self.assertEqual(binSearchResult,0)
	def testBinSearch2(self):
		weights=1,2,3
		binSearchResult=binarysearch.binarysearch(weights,0)
		self.assertEqual(binSearchResult,0)
		binSearchResult=binarysearch.binarysearch(weights,1)
		self.assertEqual(binSearchResult,1)
		binSearchResult=binarysearch.binarysearch(weights,2)
		self.assertEqual(binSearchResult,1)
		binSearchResult=binarysearch.binarysearch(weights,3)
		self.assertEqual(binSearchResult,2)
		binSearchResult=binarysearch.binarysearch(weights,4)
		self.assertEqual(binSearchResult,2)
		binSearchResult=binarysearch.binarysearch(weights,5)
		self.assertEqual(binSearchResult,2)
	def testBinSearch3(self):
		weights=5,1
		binSearchResult=binarysearch.binarysearch(weights,6)
		self.assertEqual(binSearchResult,1)

unittest.main()
