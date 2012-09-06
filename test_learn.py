#!/usr/bin/env python
# -*- coding: utf-8 -*
import unittest
import learn
class test_learn(unittest.TestCase):
	def testLearn1(self):
		sentence="テスト"
		learn.learn(sentence)
	def testLearn2(self):
		sentence="てすと"
		learn.learn(sentence)
unittest.main()
