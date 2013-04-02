#!/usr/bin/env python
# -*- coding: utf-8 -*
import csv
import codecs

tweetreader=csv.reader(open('tweets.csv','rb'))
texts=[]
for row in tweetreader:
	texts.append(row[7])
with codecs.open('fromofficialdownloadtext.txt','wb',) as f:
	rawtexts="\n".join(texts)
	f.write(rawtexts)
