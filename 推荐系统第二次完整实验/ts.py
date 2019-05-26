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
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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
import heapq
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
#print(t_mertix)
#计算每一行电影评分值的标准差，以确定该电影是否为评分波动较大的电影
non_1 = np.std(t_mertix,axis=1)
print(type(non_1))
std = non_1.tolist()
#print(std)
#将所有标准差为0的电影不计入标准差的统计范围
for i in range(0,len(std)):
    if std[i] ==0:
        std[i] = 100
    i=i+1

print(std)
#调用heapq函数，输出最小的前50个元素
print("电影ID：318的标准差为：",std[318])
print("电影ID：181的标准差为：",std[181])
print("电影ID：346的标准差为：",std[346])
print("电影ID：50的标准差为：",std[50])
print("电影ID：385的标准差为：",std[385])

#item_user1= [286,127,64,9,132,316,318,98,423,483,50,179,194,133,673,134,13,181,315,614,172,151,523,659,15,750,661,655,168,521,507,211,200,735,435,293,143,93,462,170,632,124,235,313,100,135,346,237,505,705]
#print(item_user1)






