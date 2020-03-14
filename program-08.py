#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 20:07:29 2020
This code is used to analysis the discharge of wabash river
@author: xu1361
"""

# Import necessary module
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series, DataFrame, Panel

# Read data
data = pd.read_table('WabashRiver_DailyDischarge_20150317-20160324.txt',
                     skiprows=26, sep=r"\s*", usecols=[2,3,5],
                     names=['datetime','time','discharge'])
data['timestamp']=data['datetime']+' '+data['time']
dates = pd.to_datetime(data['timestamp']) # change to datetime format
data['datetime']=dates
data = data.drop(columns=['time','timestamp'])
data.index = data['datetime'] # set datetime as index
print(data)

# Plot daily streamflow data
Daily_dis = data.resample('D').mean()
print(Daily_dis)
Daily_dis.plot(title='Daily average streamflow')
plt.ylabel('Discharge (cfs)')
plt.savefig('Daily_mean_discharge.pdf')
plt.show()

# Find out and plot the top 10 daily streamflow 
ten = Daily_dis.nlargest(10,['discharge'])
time = pd.to_datetime(ten.index)
print(ten.index)
ax = Daily_dis.plot(title='Tope 10 discharge of Daily average streamflow')
ay = plt.scatter(time, ten.discharge, color='r',label='Top 10 streamflow')
ax.legend()
#ay.legend('top 10')
plt.ylabel('Discharge (cfs)')
plt.savefig('Top_10_discharge.pdf')
plt.show()

# Plot monthly average streamflow 
Monthly_dis = data.resample('M').mean()
print(Monthly_dis)
Monthly_dis.plot(title='Monthly average streamflow')
plt.ylabel('Discharge (cfs)')
plt.savefig('Monthly_mean_discharge.pdf')
plt.show()