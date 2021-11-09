import xarray as xr
import numpy as np
import pandas as pd
import os
main_addr = r"E:\li zhen\Multi-source data Li Zhen\Daily data\CA_prep" #文件夹目录
# choose_station = np.loadtxt('choose_station.csv')

choose_station = ['KG000036974.txt','KZ000028676.txt'
]
for filename in choose_station:
    data = pd.read_csv(main_addr + r'/%s' % filename, delim_whitespace=True, header=None,
                       names=['year', 'month', 'day', 'data'])
    data[data == -9999] = np.nan
    data[data == 9999.99] = np.nan
    monthly_sum = data['data'].groupby([data['year'], data['month']]).apply(pd.DataFrame.sum, skipna=False).reindex()

    monthly_sum.to_csv(filename[:-4]+'.csv')