# MOVIELENS
# 这个项目用于展示通过训练movielens数据集对用户进行电影推荐
_项目初期，需要用到很多包，例如numpy、pandas、sklearn、os、math等等，本人是缺什么包就在cmd命令行下面pip什么包，后来在
实际运行中发现很多问题：pip自己安装的包，只安装该包所依赖的包，并非该包完整的包，在实际导入中会出现诸多can't find module这类的问题，很让人蛋疼。_

_笔者总结后给出一个这类问题的解决方案：强烈建议不要偷懒使用pip，应当去官网上自己手动下载相应的安装包后缀名为.whl
给出一个网址，该网址包含了python目前几乎所有的版本的安装包  
[Python各安装包](https://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy "Python安装包")
下载完之后再手动pip install 路径\文件名.whl_
##  一、使用pandas对数据集进行读取查看操作（查看数据集）
下载完movielens数据集后
我们先导入numpy,os,pandas这三个包对数据进行读取和查看
代码如下：
```
import numpy
import os
import pandas as pd
rating = pd.read_csv(r'F:\pythontest\movielens\ratings.csv', index_col=None)
rating.head(10)
print(rating)#读取rating文件数据
movie = pd.read_csv(r'F:\pythontest\movielens\movies.csv', index_col=None)
movie.head(10)
print(movie)#读取movie文件数据

```
代码运行截图如下：  
![pandas读取数据集]({{site.baseurl}}/https://github.com/Gaoshiguo/MOVIELENS/blob/master/movielens/1.png)  
代码运行效果图如下：
![image]({{site.baseurl}}/https://github.com/Gaoshiguo/MOVIELENS/blob/master/movielens/2.png)  
我们可以看到读取的rating文件数据的前五项包括了`<userId>` `<movieId>` `<rating>` `<timestap>`  


## 二、对数据进行预处理
我们使用`<merge>`函数对ratings和movies两个文件进行合并，关联关系使用userId，合并完之后，再将数据按比率分成训练集和测试集
具体代码如下：
```
rating_count_by_movie = data.groupby(['movieId', 'title'], as_index=False)['rating'].count()
rating_count_by_movie.columns = ['movieId', 'title', 'rating_count']
rating_count_by_movie.sort_values(by=['rating_count'], ascending=False, inplace=True)
print(rating_count_by_movie[:10])#将合并后的文件按照降序排列打印

```
![image]({{site.baseurl}}/https://github.com/Gaoshiguo/MOVIELENS/blob/master/movielens/3.png)
![image]({{site.baseurl}}/https://github.com/Gaoshiguo/MOVIELENS/blob/master/movielens/4.png)

**我们可以看到数据被分成了训练集和测试集两个部分，但是数据非常多。笔者在后期实验中发现，如此之多的数据会在矩阵运算中发生溢出**  









