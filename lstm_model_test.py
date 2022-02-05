# -*- coding: utf-8 -*-

# Import the necessary modules
import pickle
import numpy as np
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import pandas as pd
# 导入字典
with open('./data/lstm/word_dict.pk', 'rb') as f:
    word_dictionary = pickle.load(f)
with open('./data/lstm/label_dict.pk', 'rb') as f:
    output_dictionary = pickle.load(f)



input_shape = 140
# 载入模型
model_save_path = './data/lstm/douban_lstm_140.model'
lstm_model = load_model(model_save_path)


#测试集测试
mydata = pd.read_csv('data/comment_testset_2class.csv', ',', encoding='utf-8') #导入文本
mydata.reset_index()

total = 0
yes = 0
skip = 0
mydata['result'] = 0
for i in range(len(mydata)):
    try:
        curSent = mydata.loc[i,'CONTENT']
        x = [[word_dictionary[word] for word in curSent]]
        x = pad_sequences(maxlen=input_shape, sequences=x, padding='post', value=0)
        y_predict = lstm_model.predict(x)
        label_dict = {v:k for k,v in output_dictionary.items()}
        cur_predict = label_dict[np.argmax(y_predict)]
        if cur_predict == 1:
            print(''+str(i+1)+'.[^_^ 积极情感] : '+curSent+"\n")
        else:
            print(''+str(i+1)+'.[-_- 负面情感] : '+curSent+"\n")
        if cur_predict * mydata.loc[i,'label'] > 0:
            yes = yes + 1
        total = total + 1
       
    except KeyError as err:
        # print("您输入的句子有汉字不在词汇表中，请重新输入！")
        # print("不在词汇表中的单词为：%s." % err)
        skip = skip + 1
    if i >= 1999:
        break

print('\n======================================')
print('[你的名字] >2020.5.10<')
print('[总数]: '+str(total)+'  [正确数]: ' +str(yes)+'  [跳过数]: '+str(skip))
print('[模型准确率]:'+str((yes/total)*100)+'%')
print('======================================\n')



# try:
#     # 数据预处理
#     
#     sent = "电视刚安装好，说实话，画质不怎么样，很差！"
#     x = [[word_dictionary[word] for word in sent]]
#     x = pad_sequences(maxlen=input_shape, sequences=x, padding='post', value=0)



#     # 模型预测
#     y_predict = lstm_model.predict(x)
#     label_dict = {v:k for k,v in output_dictionary.items()}
#     print('输入语句: %s' % sent)
#     print('情感预测结果: %s' % label_dict[np.argmax(y_predict)])
# except KeyError as err:
#     print("您输入的句子有汉字不在词汇表中，请重新输入！")
#     print("不在词汇表中的单词为：%s." % err)


