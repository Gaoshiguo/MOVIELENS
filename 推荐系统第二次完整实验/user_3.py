import matplotlib as plot
import math
import pandas as pd
import numpy as np

item_user1= [286,
127,
64,
9,
132,
316,
318,
98,
423,
483,
50,
179,
194,
133,
673,
134,
13,
181,
315,
614,
172,
151,
523,
659,
15,
750,
661,
655,
168,
521,
507,
211,
200,
735,
435,
293,
143,
93,
462,
170,
632,
124,
235,
313,
100,
135,
346,
237,
505,
705]
print(item_user1)
predic_values=[5.0,
4.6666665,
4.5,
4.5,
4.5,
4.5,
4.5,
4.5,
4.5,
4.5,
4.0,
4.0,
4.0,
4.0,
4.0,
4.0,
4.0,
4.0,
4.0,
4.0,
3.6666667,
3.6666667,
3.5,
3.5,
3.5,
3.5,
3.5,
3.5,
3.5,
3.5,
3.5,
3.5,
3.5,
3.5,
3.5,
3.5,
3.5,
3.5,
3.5,
3.5,
3.5,
3.5,
3.5,
3.5,
3.3333333,
3.0,
3.0,
3.0,
3.0,
3.0]
#print(predic_values)
#读取拆分的测试集
true_values = pd.read_csv(r'D:\Python代码练习\u_v_test.data',sep='\t')
#print(true_values)
#true_values是一个pandas中的datafram数据类型，将其转换成一个矩阵类型，使用
#numpy 库的array（）函数，可以直接将数据类型转换成矩阵类型。
values = np.array(true_values)
#我们第一步之观测用户1的数据，先获取用户1的真实电影id和评分
list_1=[]
for i in range(0,len(values)):
    if values[i][0] ==3:
        list_1.append(values[i][1])
        #print(values[i][1])
    i=i+1
print(list_1)
list_2=[]
for i in range(0,len(values)):
    if values[i][0] ==3:
        list_2.append(values[i][2])
        #print(values[i][2])
    i=i+1
print(list_2)
#构造一个函数来计算MAE
def calc_MAE(list_one,list_two,list_three,list_four):
    predicvalue=[]
    truevalue=[]
    for i in range(0, len(list_one)):
        for j in range(0, len(list_two)):
            if list_one[i] == list_two[j]:
                print('成功命中测试集的电影id为',item_user1[i])
                predicvalue.append(list_three[i])
                truevalue.append(list_four[j])
        j = j + 1
    i = i + 1
    print("预测的电影评分值为：",predicvalue)
    print("测试集中真实的评分值为：",truevalue)
    sum =0
    for i in range(0,len(predicvalue)):
        va=abs(predicvalue[i]-truevalue[i])
        sum = sum+va
        i=i+1
    mae=sum/len(predicvalue)
    print("计算得到的mae的值为：",mae)
calc_MAE(item_user1,list_1,predic_values,list_2)


