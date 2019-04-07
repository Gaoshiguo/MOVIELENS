import numpy as np
import pandas
array = [
    [5,3,4,4],
    [3,1,2,3],
    [4,3,4,3],
    [3,3,1,5],
    [1,5,5,2]
]

new_array = [
    [5,3,4,4],
    [3,1,2,3,3],
    [4,3,4,3,5],
    [3,3,1,5,4],
    [1,5,5,2,1]


]
cor = np.corrcoef(array)
print(cor)
list = [ ]
for i in range(0,4):
    if cor[0][i]>0 and cor[0][i]<1 :
        list.append(i)
    i = i+1
print(list)

list_1 = []
for i in range(0,len(list)):
    sum(new_array[list[i]])
    average = sum(new_array[list[i]])/len(new_array[list[i]])
    list_1.append(average)
    i = i+1
print(list_1)

pre = 0
for i in range(0,len(list_1)-1):
    pre =pre+(cor[0][list[i]]*(new_array[list[i]][4]-list_1[i]))
    i = i+1

print(pre)
list_2 = []
for i in range(0,len(list)):
    list_2.append(cor[0][list[i]])
    i = i+1
print(list_2)
predict = (sum(new_array[0])/len(new_array[0]))+(pre/sum(list_2))
print(predict)








