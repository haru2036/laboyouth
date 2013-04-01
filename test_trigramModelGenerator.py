#!/usr/bin/env python
# -*- coding: utf-8 -*
import unittest
from datetime import datetime
import trigramModelGenerator
import codecs
import mecabCaller
class test_trigramModelGenerator(unittest.TestCase):
	def setUp(self):
		self.sentence=[]
		self.itemlist=["A","B","C","C","D","A","B","B","A","D","C","B","C","A","D","A","C","D","B","D","A","A","D"]
		with codecs.open("strarf_serif.txt",'rb','utf-8') as f:
			for line in f:
				self.sentence.append(line)
				self.sentence.append(u"EOS")
		self.itemlistsentence=mecabCaller.parse(self.sentence)
	def test_generateModel_SpaceSaving(self):
		time_start=datetime.now()
		modelgen=trigramModelGenerator.modelgenerator()
		gen=modelgen.GeneratorForTrigram(self.itemlistsentence)
		result_default=modelgen.nativecounting(gen)
		time_defaultEnded=datetime.now()
		modelgen2=trigramModelGenerator.modelgenerator()
		gen2=modelgen2.GeneratorForTrigram(self.itemlistsentence)
		result_SS=modelgen2.SpaceSaving(gen2,10000)
		result_cj2freq=modelgen2.cjtofreq(result_SS.items())
		time_SSEnded=datetime.now()
		print time_start,time_defaultEnded,time_SSEnded
		time_default=time_defaultEnded - time_start
		time_SS=time_SSEnded - time_defaultEnded
		print 'Default,SS'
		print time_default,time_SS
	def test_generateModel_SpaceSavingUsingGenerator(self):
		modelgenunigram=trigramModelGenerator.modelgenerator()
		unigramgen=modelgenunigram.GeneratorForUnigram(self.itemlist)
		SS=modelgenunigram.SpaceSaving(unigramgen,3)
		print modelgenunigram.buckets
		self.assertEqual(modelgenunigram.minimum,7)
	def test_unigramtest2(self):
		itemlist=["B","A","C","D","B","C","C","A","D","A","C","B","C","D"]
		modelgen=trigramModelGenerator.modelgenerator()
		gen=modelgen.GeneratorForUnigram(itemlist)
		SS=modelgen.SpaceSaving(gen,3)
		self.assertEqual(modelgen.minimum,min(modelgen.cj.values()))
	def test_unigramtest3(self):
		itemlist=["A","A","B","A","C"]
		modelgen=trigramModelGenerator.modelgenerator()
		gen=modelgen.GeneratorForUnigram(itemlist)
		SS=modelgen.SpaceSaving(gen,3)
		self.assertEqual(modelgen.minimum,min(modelgen.cj.values()))
		valueslist=modelgen.buckets.values()
		self.assertTrue(all(len(x)>0 for x in valueslist))
		print valueslist
unittest.main()
