import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import os
import matplotlib as plt
import math
from math import sqrt
from sklearn.model_selection import train_test_split
from numpy import *
from numpy import array as matrix, arange

#建立一个表名为“u_cols”，表中各表项为：ID,age,sex,occupation,zip_code////该表读取数据集
#中用户表，用户表中内容包括ID,age,sex,occupation,zip_code这几项
u_cols = ['user_id', 'movie_id', 'rating','timestamp']
users = pd.read_csv(r'D:\Python代码练习\train.data', names=u_cols, sep="\t", encoding='latin_1')
#read_csv中各参数分别代表的意思是：路径、文件名、sep表示各项之间使用什么字符分隔开，encoding代表编码字符格式



#建立用户电影评分二维矩阵，index为索引,设置各表项为'user_id', 'movie_id',矩阵中
trainRatingsPivotdata =pd.pivot_table(users[['user_id', 'movie_id','rating','timestamp']],columns=['movie_id'],index=['user_id'],values='rating',fill_value=None)
moviesMap = dict(enumerate(list(trainRatingsPivotdata.columns)))
usersMap = dict(enumerate(list(trainRatingsPivotdata.index)))
ratingValues = trainRatingsPivotdata.values.tolist()
#print(trainRatingsPivotdata)
#print(trainRatingsPivotdata.query('user_id==["822"]'))
#userSimMatrix=np.corrcoef(trainRatingsPivotdata)
#np.corrcoef(trainRatingsPivotdata)

mertix =zeros((943,1615))
print(mertix)
#将用户评分存储在一个矩阵之中
mertix=trainRatingsPivotdata
print(mertix)
#print(np.std(mertix, axis=0))#计算每一列的标准差
#将矩阵转置
t_mertix=np.transpose(mertix)
print(t_mertix)
#计算每一行电影评分值的标准差，以确定该电影是否为评分波动较大的电影
non_1 = np.std(t_mertix,axis=1)
print(non_1)


non_mertix = non_1
print(non_mertix)
print("用户评分波动最小的前20部电影分别为",non_mertix.nsmallest(20).index.values)





