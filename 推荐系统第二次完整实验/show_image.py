import matplotlib.pyplot as plt
import numpy as np
import matplotlib
tuijian_number = [28,28,50,25,12,15,20,10,50,21,10,16,5,17,14,23,15,27,50,28]
mingzhong_number = [2,0,3,1,0,1,2,0,2,2,1,0,4,1,0,0,0,0,2,0]
biaozhuncha_3 = [1.0974838805259368,0.936090601772688,1.083097410208334,1.1500879670536472,0.8414348907780932]
mae_3 = [0.5,0,2,1,0]
mingzhong_rate = []
for i in range(0,len(tuijian_number)):
    mingzhong_rate.append((mingzhong_number[i])/(tuijian_number[i]))
    i=i+1
print(mingzhong_rate)
mae = [1.5,0,0.8333334,3,0,0.4558442,1.41666665,0,0.5,1.333325,0,0,1.45,0.25,0,0,0,0,1.25,0]
plt.figure()
matplotlib.rcParams['font.family'] = 'SimHei'
plt.scatter(tuijian_number,mae,s=100,color="black",marker="o")
plt.xlabel("推荐电影数量：部")
plt.ylabel("MAE值")
plt.title("电影数目与MAE的关系图")
plt.show()

plt.figure()
matplotlib.rcParams['font.family'] = 'SimHei'
plt.scatter(mingzhong_rate,mae,s=100,color="black",marker="o")
plt.xlabel("推荐电影命中率：%")
plt.ylabel("MAE值")
plt.title("推荐电影命中率与MAE的关系图")
plt.show()

plt.figure()
matplotlib.rcParams['font.family'] = 'SimHei'
plt.scatter(biaozhuncha_3,mae_3,s=100,color="black",marker="o")
plt.xlabel("标准差")
plt.ylabel("MAE值")
plt.title("标准差与MAE的关系图")
plt.show()