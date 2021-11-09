import xarray as xr
import numpy as np
import pandas as pd
import os

year_length_thre = 20
year_nan_thre = 10


main_addr = r"E:\li zhen\Multi-source data Li Zhen\Daily data\PREP" #文件夹目录


files= os.listdir(main_addr)

def select(data):

    if data['year'].unique().shape[0] < year_length_thre:#1 unique函数去除其中重复的元素，并按元素由大到小返回一个新的无元素重复的元组或者列表shape[0]输出3，为矩阵的行数
        return False

    data[data == 9999.99] = np.nan
    data[data == -9999] = np.nan
    def find_nan(x):
        x = pd.DataFrame(x)#生成一个表格
        a = x.isna().sum()#每列有多少缺失值
        return a

    a = data['data'].groupby(data['year']).apply(lambda x: find_nan(x))#groupby分组 lambda x，每个字符串去空格处理

    if a.min() >= year_nan_thre:#365
        return False
    else:
        return True

choose_station = []

for filename in files:
    data = pd.read_csv(main_addr + r'/%s' % filename, delim_whitespace=True, header=None,
                       names=['year', 'month', 'day', 'data'])
    judge = select(data)
    if judge:
        print(filename)
        choose_station.append(filename)
    test = pd.DataFrame(data=choose_station)
    test.to_csv(filename[:-4]+'.csv', encoding='gbk')
