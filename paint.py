import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import operator
from functools import reduce
data=pd.read_csv("E:\project\\try.csv")
 #必须添加header=None，否则默认把第一行数据处理成列名导致缺失
data=data.drop(["800"], axis=1)
list=data.values.tolist()
# print(list)
list_1=reduce(operator.add, list)

arr = np.array(list_1) # 转换成array
key = np.unique(list_1)  # x轴，得到的也是array对象
result = {}
for k in key:
    mask = (arr == k)
    arr_new = arr[mask]
    v = arr_new.size
    result[k] = v
print(result)
#result是类似于这样的字典：{外语学院：15，文学院：23.....}
x = key # 取院系的那一列key1 in adict
y = result.values() # 取数字的那一列
plt.bar(x, y, align='center') # 画图，设置x，y轴的数据
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
for x, y in zip(x, y):
    plt.text(x, y+0.05, '%.0f'%y, ha='center', va='bottom')
plt.xticks(range(1880,2018,5),rotation =0)# rotation设置x轴标签的旋转度数

plt.show()

# plt.hist(list)
# plt.xlabel('scores')
# plt.ylabel('count')



# print(list[2])
# print(list[1]+list[2])
# print(len(list))
