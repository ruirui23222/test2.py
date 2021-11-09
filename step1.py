import xarray as xr
import numpy as np
import pandas as pd
import os

year_length_thre = 10
year_nan_thre = 365


main_addr = r"E:\li zhen\Multi-source data Li Zhen\Daily data\CA_prep" #文件夹目录


files= os.listdir(main_addr)

def select(data):

    if data['year'].unique().shape[0] < year_length_thre:
        return False

    data[data == 9999.99] = np.nan
    data[data == -9999] = np.nan
    def find_nan(x):
        x = pd.DataFrame(x)
        a = x.isna().sum()
        return a

    a = data['data'].groupby(data['year']).apply(lambda x: find_nan(x))

    if a.max() <= year_nan_thre:
        return True
    else:
        return False

choose_station = []

for filename in files:
    data = pd.read_csv(main_addr + r'/%s' % filename, delim_whitespace=True, header=None,
                       names=['year', 'month', 'day', 'data'])
    judge = select(data)
    if judge:
        print(filename)
        choose_station.append(filename)
print(choose_station)

np.savetxt('choose_station.csv', choose_station)

choose_station = np.loadtxt('choose_station.csv')
#
#
# for filename in choose_station:
#     data = pd.read_csv(main_addr + r'/%s' % filename, delim_whitespace=True, header=None,
#                        names=['year', 'month', 'day', 'data'])
#     data[data == -9999] = np.nan
#     data[data == -9999.99] = np.nan
#     monthly_sum = data['data'].groupby([data['year'], data['month']]).apply(pd.DataFrame.sum, skipna=False).reindex()
#
#     monthly_sum.to_csv(filename[:-4]+'.csv')