import numpy
import os
import pandas as pd
rating = pd.read_csv(r'F:\pythontest\movielens\ratings.csv', index_col=None)
rating.head(10)
print(rating)#读取rating文件数据
movie = pd.read_csv(r'F:\pythontest\movielens\movies.csv', index_col=None)
movie.head(10)
print(movie)#读取movie文件数据
data = pd.merge(rating,movie, on='movieId')
print(data)#将rating和movie文件合并
rating_count_by_movie = data.groupby(['movieId', 'title'], as_index=False)['rating'].count()
rating_count_by_movie.columns = ['movieId', 'title', 'rating_count']
rating_count_by_movie.sort_values(by=['rating_count'], ascending=False, inplace=True)
print(rating_count_by_movie[:10])#将合并后的文件按照降序排列打印

