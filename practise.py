#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import sqlite3

#创建一个数据库
conn=sqlite3.connect('test.db')
print('open database successfully!')

#添加tags数据集，并连接到sqlite
tags=pd.read_csv('C:/Users/Administrator/Desktop/recommender-sys/movielens/tags.csv')
tags.to_sql('tags',conn,if_exists='append', index=False)
print(tags[:10])
print()

#添加ratings数据集，并连接到sqlite
ratings=pd.read_csv('C:/Users/Administrator/Desktop/recommender-sys/movielens/ratings.csv')
ratings.to_sql('ratings',conn,if_exists='append',index=False)
print(ratings[:10])
print()

#添加movies数据集，并连接到sqlite
movies=pd.read_csv('C:/Users/Administrator/Desktop/recommender-sys/movielens/movies.csv')
movies.to_sql('movies',conn,if_exists='append',index=False)
print(movies[:10])
print()

#添加links数据集，并连接到sqlite
links=pd.read_csv('C:/Users/Administrator/Desktop/recommender-sys/movielens/links.csv')
links.to_sql('links',conn,if_exists='append',index=False)
print(links[:10])
print()

#计算用户和项目的唯一数量
users=ratings.userId.unique().shape[0]
items=ratings.movieId.unique().shape[0]
print('number of users='+str(users)+'||number of movies='+str(items))
print()

#添加ratings数据集，并连接到sqlite
ratingsasc=pd.read_csv('C:/Users/Administrator/Desktop/recommender-sys/movielens/ratingsasc.csv')
ratings.to_sql('ratingsasc',conn,if_exists='append',index=False)
print(ratingsasc[:10])
print()

#将ratings评分数据集随机划分8:2
from sklearn.model_selection import train_test_split
train, test = train_test_split(ratingsasc, test_size=0.2)
print(train[:10])
print(test[:10])

#分别建立测试集和训练集的用户——项目矩阵
train_matrix=np.zeros((users,items))
for line in train.itertuples():
    train_matrix[line[1]-1,line[2]-1]=line[3]
test_matrix=np.zeros((users,items))
for line in test.itertuples():
    test_matrix[line[1]-1,line[2]-1]=line[3]

