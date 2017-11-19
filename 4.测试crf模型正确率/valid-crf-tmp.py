#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import os
import sys
import io
import re

from pandas import Series, DataFrame 
import jieba
import jieba.posseg as pseg


path = "C:/word2vec/pyltp";
train_file = "̩һָ��-���⼯.csv"
jieba.load_userdict(path+'/model/nopos_word_file.txt')

file = open(path+'/��˼·����/4.����crfģ����ȷ��/crf_valid2.csv',encoding="UTF-8")
topic_word_crf_train_valid_file = open(path+'/��˼·����/4.����crfģ����ȷ��/code/��֤train.txt', 'w+',encoding='UTF-8')

print("��ʼ����������...")

data = []
index = 1

T = []
S = []
TISEXEC=False
T_count = 0
S_count = 0
while 1:
	line = file.readline().strip()	
	if not line and line == "":
		print("---------------------->"+str(index)+"---"+str(T)+"---"+str(S))
		print(index)
		while len(T) != len(S):
			# ���ֻ��һ��Sһ��T������ע˳��
			print("T_count��"+str(T_count)+", S_count:"+str(T_count))
			if T_count == 1 and S_count == 1:
				print("һ��Sһ��T")
				T.remove("NULL")
			elif T_count == 0 and S_count == 0:
				print("��S��T")
			elif len(T) > len(S):
				S.append("NULL")
		txt = ""
		for ttt in T:
			txt = txt+ttt+";"
		sxs = ""
		for sss in S:
			sxs = sxs+sss+";"
		topic_word_crf_train_valid_file.write(str(index)+","+txt+","+sxs+"\n")
		
		index = index+1
		T = []
		S = []
		T_count = 0
		S_count = 0
		break
		#continue
	lines = line.split("\t")
	word = lines[0]
	pos = lines[1]
	tag = lines[2]
	print(word+"\t"+pos+"\t"+tag)
	
	if pos == "x":# ������
				
	if tag == "T":
		T.append(word)
		T_count = T_count+1
		TISEXEC=True
	elif tag == "S":
		# T����Ϊ��
		S_count = S_count+1
		if TISEXEC == False:
			print("===>"+word)
			T.append("NULL")
			S.append(word)
			TISEXEC=False
			#print(T+":"+S)
		else:
			#print("NULL"+":"+S)
			S.append(word)
			TISEXEC=False

		
	
	

topic_word_crf_train_valid_file.flush()
topic_word_crf_train_valid_file.close()
	
	
	
	