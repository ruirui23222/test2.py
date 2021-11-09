# 这一步主要是求月平均  不需要月平均可以不要
import xarray as xr
import numpy as np
import pandas as pd
import os
main_addr = r"E:\li zhen\Multi-source data Li Zhen\Daily data\PREP" #文件夹目录
# choose_station = np.loadtxt('choose_station.csv')

choose_station = ['277850.txt', '286760.txt']

for filename in choose_station:
    data = pd.read_csv(main_addr + r'/%s' % filename, delim_whitespace=True, header=None,
                       names=['year', 'month', 'day', 'data'])
    test = pd.DataFrame(data)
    test.to_csv(filename[:-4]+'.csv', encoding='gbk')