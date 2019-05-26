import matplotlib as plot
import math
import pandas as pd
import numpy as np

item_user1= [313,272,286,332,323,302,258,329,905,331,898,311,315,340,347,288,751,289,346,300,895,301,307,327,326,343,328,358]
#print(len(item_user1))
predic_values=[5.0,5.0,5.0,4.5,4.5,4.5,4.0,4.0,4.0,4.0,4.0,4.0,4.0,4.0,4.0,3.7,3.5,3.5,3.5,3.5,3.3333333,3.25,3.0,2.6666667,2.5,2.5,2.5,1.0]
#print(len(predic_values))
#读取拆分的测试集
true_values = pd.read_csv(r'D:\Python代码练习\u_v_test.data',sep='\t')
#print(true_values)
#true_values是一个pandas中的datafram数据类型，将其转换成一个矩阵类型，使用
#numpy 库的array（）函数，可以直接将数据类型转换成矩阵类型。
values = np.array(true_values)
#我们第一步之观测用户1的数据，先获取用户1的真实电影id和评分
list_1=[]
for i in range(0,len(values)):
    if values[i][0] ==1:
        list_1.append(values[i][1])
        #print(values[i][1])
    i=i+1
print(list_1)
list_2=[]
for i in range(0,len(values)):
    if values[i][0] ==1:
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
    #print(predicvalue)
    #print(truevalue)
    sum =0
    for i in range(0,len(predicvalue)):
        va=abs(predicvalue[i]-truevalue[i])
        sum = sum+va
        i=i+1
    mae=sum/len(predicvalue)
    print("计算得到的mae的值为：",mae)
calc_MAE(item_user1,list_1,predic_values,list_2)


