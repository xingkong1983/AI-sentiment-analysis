#-*- coding: utf-8 -*-

import numpy as np #导入numpy
import pandas as pd
import jieba
from tqdm import tqdm
#预处理基本结束

#开始加载情感词典
negdict = [] #消极情感词典
posdict = [] #积极情感词典
nodict = [] #否定词词典
plusdict = [] #程度副词词典
sl = pd.read_csv('dict/neg.txt', header=None, encoding='utf-8')
# print(sl.head(3))
# print(sl.shape)
for i in range(len(sl[0])):
	negdict.append(sl[0][i])

sl = pd.read_csv('dict/pos.txt', header=None, encoding='utf-8')
for i in range(len(sl[0])):
	posdict.append(sl[0][i])
sl = pd.read_csv('dict/no.txt', header=None, encoding='utf-8')
for i in range(len(sl[0])):
	nodict.append(sl[0][i])
sl = pd.read_csv('dict/plus.txt', header=None, encoding='utf-8')
for i in range(len(sl[0])):
	plusdict.append(sl[0][i])
#加载情感词典结束


#预测函数
def predict(str, negdict, posdict, nodict, plusdict):
	score = 0
	sd = list(jieba.cut(str))
	for i in range(len(sd)):
		if sd[i] in negdict:
			if i>0 and sd[i-1] in nodict:
				score = score + 1
			elif i>0 and sd[i-1] in plusdict:
				score = score - 2
			else: score = score - 1
		elif sd[i] in posdict:
			if i>0 and sd[i-1] in nodict:
				score = score - 1
			elif i>0 and sd[i-1] in plusdict:
				score = score + 2
			elif i>0 and sd[i-1] in negdict:
				score = score - 1
			elif i<len(sd)-1 and sd[i+1] in negdict:
				score = score - 1
			else: score = score + 1
		elif sd[i] in nodict:
			score = score - 0.5
	return score
#预测函数结束

# #测试集测试
mydata = pd.read_csv('data/comment_testset_2class.csv', ',', encoding='utf-8') #导入文本
mydata.reset_index()

total = 0
yes = 0
mydata['result'] = 0
for i in tqdm(range(len(mydata))):
	cur_content = mydata.loc[i,'CONTENT']
	cur_label = mydata.loc[i,'label']
	total = total + 1
	cur_predict = predict(cur_content, negdict, posdict, nodict, plusdict)
	if cur_predict * cur_label > 0:
		yes = yes + 1
		
print(yes/total)

#简单的测试
p = predict("我今天很开心", negdict, posdict, nodict, plusdict)
print(p)

p = predict("我今天不高兴", negdict, posdict, nodict, plusdict)
print(p)
