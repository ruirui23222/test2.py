# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import netCDF4
from netCDF4 import Dataset
nc_obj=Dataset('F:\OneDrive\Python\A\\albisccp_cfDay_CanESM2_historical_r1i1p1_19790101-20051231 2.0.nc')

#查看nc文件有些啥东东
print(nc_obj)
print('---------------------------------------')

#查看nc文件中的变量
print(nc_obj.variables.keys())
for i in nc_obj.variables.keys():
    print(i)
print('---------------------------------------')

#查看每个变量的信息
print(nc_obj.variables['lat'])
print(nc_obj.variables['time'])

print('---------------------------------------')

# #查看每个变量的属性
# print(nc_obj.variables['LAT'].ncattrs())
# print(nc_obj.variables['LON'].ncattrs())
# print(nc_obj.variables['PRCP'].ncattrs())
# print(nc_obj.variables['LAT'].units)
# print(nc_obj.variables['LON'].units)
# print(nc_obj.variables['PRCP']._Fillvalue)
# print('---------------------------------------')
#
#读取数据值
lat=(nc_obj.variables['lat'][:])
lon=(nc_obj.variables['lon'][:])
prcp=(nc_obj.variables['albisccp'][:])
# print(lat)
# print(lon)
print('---------------******-------------------')
print(prcp)
