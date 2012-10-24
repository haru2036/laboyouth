#!/usr/bin/env python
# -*- coding: utf-8 -*

import unittest
import sentenceGenerator

class test_sentenceGenerator(unittest.TestCase):
	def testBigram1(self):
		freq1={u"テスト":{u"テスト":{u"テスト":1}}}
		keyword=u"テスト"
		sentenceGen=sentenceGenerator.sentenceGenerator(freq1,keyword)
		bigramResult=sentenceGen.bigram(keyword)
		self.assertEqual(bigramResult,u"テスト")
	def testBigram2(self):
		freq1={u"テスト":{u"foo":{u"foo":1}}}
		keyword=u"テスト"
		sentenceGen=sentenceGenerator.sentenceGenerator(freq1,keyword)
		bigramResult=sentenceGen.bigram(keyword)
		self.assertEqual(bigramResult,u"foo")
	def testSentenceGenerator(self):
		freq1={u"テスト":{u"foo":{u"foo":1}},u"foo":{u"foo":{u"foo":1}}}
		keyword="テスト"
		sentenceGen=sentenceGenerator.sentenceGenerator(freq1,keyword)
		sentence=sentenceGen.generateSentence()
		self.assertEqual(len(sentence),12)
		self.assertEqual(sentence[0],u"テスト")
		self.assertEqual(sentence[1],u"foo")
		self.assertEqual(sentence[2],u"foo")
		self.assertEqual(sentence[3],u"foo")
		self.assertEqual(sentence[4],u"foo")
		self.assertEqual(sentence[5],u"foo")
		self.assertEqual(sentence[6],u"foo")
		self.assertEqual(sentence[7],u"foo")
		self.assertEqual(sentence[8],u"foo")
		self.assertEqual(sentence[9],u"foo")
	"""単語がモデルに見当たらなかったときのエラー動作の確認（１単語目の時)"""
	def testNoWord(self):
		freq1={u"foo":{u"foo":{u"foo":1}}}
		keyword=u"あーてすてす"
		sentenceGen=sentenceGenerator.sentenceGenerator(freq1,keyword)
		sentence=sentenceGen.generateSentence()
		self.assertIn("Error1",sentence)
	"""単語がモデルに見当たらなかったときのエラー動作の確認（２単語目の時）"""
	def testNoWord2(self):
		freq1={u"あーてすてす":{u"foo":{u"bar":1}}}
		keyword=u"あーてすてす"
		sentenceGen=sentenceGenerator.sentenceGenerator(freq1,keyword)
		sentence=sentenceGen.generateSentence()
		self.assertIn("Error2",sentence)
unittest.main()
