import numpy as np
import os
import pandas as pd
import math
from sklearn.model_selection import train_test_split
ratingpath = r'F:\pythontest\movielens\ratings.csv'#用ratingpath变量来存储rating文件的路径
moviespath = r'F:\pythontest\movielens\movies.csv'#用moviegpath变量来存储movies文件的路径
ratingsData = pd.read_csv(ratingpath, index_col=None)#用ratingData变量存储rating文件
moviessData = pd.read_csv(moviespath, index_col=None)#用moviesData变量存储movies文件

#数据集中的数据太大，在建立矩阵时发生溢出。我们使用pandas对数据进行预处理，
# 调用pandas中的sample函数，随机提取整个样本文件的0.01%的数据作为样本
ratingData =ratingsData.sample(n=None,frac=0.0001,replace=False,weights=None,random_state=None,axis=None)
movieData =moviessData.sample(n=None,frac=0.0001,replace=False,weights=None,random_state=None,axis=None)

#将文件二八开分为训练集和测试集
trainratingData,testratingData = train_test_split(ratingData,test_size=0.3)
print(trainratingData,testratingData)
print('total_movie_count:'+str(len(set(ratingData['movieId'].values.tolist()))))
print("total_user_count:"+str(len(set(ratingData['userId'].values.tolist()))))
print("train_movie_count:"+str(len(set(trainratingData['movieId'].values.tolist()))))
print("train_user_count:"+str(len(set(trainratingData['userId'].values.tolist()))))
print("test_movie_count:"+str(len(set(testratingData['movieId'].values.tolist()))))
print("test_movie_count:"+str(len(set(testratingData['userId'].values.tolist()))))


#建立用户电影评分矩阵，建立电影ID和用户ID的对应关系

trainRatingsPivotdata =pd.pivot_table(trainratingData[['userId','movieId','rating']],columns=['movieId'],index=['userId'],values='rating',fill_value=0)
moviesMap = dict(enumerate(list(trainRatingsPivotdata.columns)))
usersMap = dict(enumerate(list(trainRatingsPivotdata.index)))
ratingValues = trainRatingsPivotdata.values.tolist()

#定义函数计算用户相似度
def calCosineSimilarity(list1,list2):
    res = 0
    denominator1 = 0
    denominator2 = 0
    for (val1,val2) in zip(list1,list2):
        res += (val1 * val2)
        denominator1 += val1 ** 2
        denominator2 += val2 ** 2
    return res / (math.sqrt(denominator1 * denominator2))

用户相似度矩阵是一个上三角矩阵对角线元素为0
userSimMatrix = np.zeros((len(ratingValues),len(ratingValues)),dtype=np.float32)
for i in range(len(ratingValues)-1):
    for j in range(i+1,len(ratingValues)):
        userSimMatrix[i,j] = calCosineSimilarity(ratingValues[i],ratingValues[j])
        userSimMatrix[j,i] = userSimMatrix[i,j]

userMostSimDict = dict()
for i in range(len(ratingValues)):
    userMostSimDict[i] = sorted(enumerate(list(userSimMatrix[0])),key = lambda x:x[1],reverse=True)[:10]

#计算推荐权值
userRecommendValues = np.zeros((len(ratingValues),len(ratingValues[0])),dtype=np.float32)
for i in range(len(ratingValues)):
    for j in range(len(ratingValues[i])):
        if ratingValues[i][j] == 0:
            val = 0
            for (user,sim) in userMostSimDict[I]:
                val += (ratingValues[user][j] * sim)
            userRecommendValues[i,j] = val

#为每个用户推荐十部电影
userRecommendDict = dict()
for i in range(len(ratingValues)):
    userRecommendDict[i] = sorted(enumerate(list(userRecommendValues[i])),key = lambda x:x[1],reverse=True)[:10]

#为索引的用户id和电影id转换为真正的用户id和电影id
userRecommendList = []
for key,value in userRecommendDict.items():
    user = usersMap[key]
    for (movieId,val) in value:
        userRecommendList.append([user,moviesMap[movieId]])


#我们将推荐结果的电影id转换成对应的电影名，并打印结果
recommendDF = pd.DataFrame(userRecommendList,columns=['userId','movieId'])
recommendDF = pd.merge(recommendDF,moviesDF[['movieId','title']],on='movieId',how='inner')
recommendDF.tail(10)