import xarray as xr
import numpy as np
import pandas as pd
import os

year_length_thre = 20
year_nan_thre = 10


main_addr = r"E:\li zhen\Multi-source data Li Zhen\Daily data\CA_prep 1.0" #文件夹目录


files= os.listdir(main_addr)

def select(data):

    if data['year'].unique().shape[0] < year_length_thre:
        return [False, None]

    data[data == 9999.99] = np.nan
    data[data == -9999] = np.nan
    def find_nan(x):
        x = pd.DataFrame(x)
        a = x.isna().sum()
        return a

    a = data['data'].groupby(data['year']).apply(lambda x: find_nan(x)).reset_index()
    if len(a[a['data']<year_nan_thre]) > 20:

        return [True, a[a['data']<=year_nan_thre].year.unique()]
    else:
        return [False, None]

choose_station = pd.DataFrame()
for filename in files:
    data = pd.read_csv(main_addr + r'/%s' % filename, delim_whitespace=True, header=None,
                       names=['year', 'month', 'day', 'data'])
    judge = select(data)

    if judge[0]:
        print(judge[1])
        print(filename)
        sdf = pd.DataFrame()
        sdf[filename[:-4]]=judge[1]
        choose_station = pd.concat([choose_station, sdf], axis=1)

choose_station.T.to_csv('try.csv')


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