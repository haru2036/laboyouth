#!/usr/bin/env python
# -*- coding: utf-8 -*
import random
def binarysearch(weights,random1=None):
	#print weights
	weightsum=0
	weightlist=[]
	for i,x in enumerate(weights):
		weightlist.append(weightsum)
		weightsum+=x
	if random1==None:
		random1=random.randint(0,weightsum-1)
	#print weightlist
	#二分探索開始
	weightlen=len(weightlist)
	#上の端っこ
	num2=weightlen
	num1=0
	#print random1
	#num1とnum2の差が1になったら終了
	while (num2-num1)!=1:
		#numの二つのインデックスの中間をmidとする
		mid=(num1+num2)/2
		#print mid,weightlist[mid]
			#中間値よりrandom1が大きいか小さいか
		if random1<weightlist[mid]:
			num2=mid
		else:
			num1=mid
	   # print num1,num2
	return num1


