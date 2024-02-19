# -*- truncate-lines:t -*-
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 11:34:18 2020
@author: Sila
"""

from modsim import *

from pandas import read_csv
import matplotlib.pyplot as plt

filename = 'World_population_estimates (1).csv'
table = read_csv(filename, header=0, index_col=0, decimal='M')
print(len(table))

#tables.columns = ['Year','census','prb','un','maddison','hyde','tanton','biraben','mj','thomlinson','durand','clark']

table['census'].plot()
plt.show()

census = table.census
print(census.head())

total_growth = census[2016] - census[1950]

print(total_growth)

t_0 = get_first_label(census)
print(t_0)
t_end = get_last_label(census)
elapsed_time = t_end - t_0
print(elapsed_time)

p_0 = get_first_value(census)
p_end = get_last_value(census)

total_growth = p_end - p_0
annual_growth = total_growth / elapsed_time

#Now let's create a TimeSeries to contain values generated by a linear growth model.

results = TimeSeries()
results[t_0] = census[t_0]

for t in linrange(t_0, t_end):
    results[t+1] = results[t] + annual_growth

table['census'].plot()
results.plot()
plt.show()


