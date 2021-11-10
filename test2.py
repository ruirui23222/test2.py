import xarray as xr
import numpy as np
import os
def find_nan(data):
    data = np.array(data)
    size_nan = np.argwhere(data==9999.99).flatten().shape#argwhere 有问题的位置在哪里 flatten()把它变成一维  shape读取矩阵的长度
    return size_nan

thre = 50
main_addr = r"E:\li zhen\Multi-source data Li Zhen\Daily data\CA_prep" #文件夹目录 CA_prep也是文件夹目录


files= os.listdir(main_addr)#返回指定的文件夹包含的文件或文件夹的名字的列表

choose_station = [] #建立一个 空数组
for filename in files:
    s_data = np.loadtxt(main_addr+'/%s'%filename)[:,3]#第三列的数据
    s_year = np.loadtxt(main_addr + '/%s' % filename)[:, 0]#地0列的年份
    year = s_year[s_data==999.99]#找出是空数据的年份
    num = []# 建立一个空数组
    for i in range(1936,2018,1):
        num.append(year.count(i))#给数组加上内容  找到空数组
    num = np.array(num)
    size_nan = np.argwhere(num>10).flatten().shape
    if size_nan[0]>0:
        continue
    else:
        # 保存
        print(filename)
        choose_station.append(filename)
print(choose_station)