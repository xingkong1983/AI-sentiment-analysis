# ai-sentiment-analysis
一个完整的句子的情感分析。
这里包含了两种方式来进行情感分析，一种是基于情感词典进行情感分析，一种是基于 lstm 进行情感分析，你可以很方便的对比这两种方式的本质区别。
lstm 基于 keras 和 tensorflow 。

## 环境搭建
请参考 python安装.txt 文件。  

## 数据  
目前数据都存放在 data 目录中。  
- 训练数据 comment_trainset_2class.csv  
- 测试数据 comment_testset_2class.csv  
- lstm模型文件名称  douban_lstm_140.model   
- 中间文件 work_dict.pk label_dict.pk
- 句子长度及出现频数统计图.png
- 句子长度累积分布函数图.png
- lstm 模型图片 model_lstm.png

## 代码
- 句子画图 lstm_sentece_plot.py
- lstm 模型训练 lstm_model_train.py
- lstm 模型测试 lstm_model_test.py
- 普通的基于词典的情感分析 qgcd.py
- tensorflow 基础测试 tensorflow-test.py
