# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np


# 带有重复索引的时间序列，通过groupby进行分组，level等于0，对分组后的数据进行计算
str_dates = ['20160101', '20170101', '20170101', '20170102', '20170102', '20170303']
dates = pd.DatetimeIndex(str_dates)
print dates
df = pd.DataFrame(np.random.rand(6, 6), index=dates, columns=np.arange(6))
print df
print df.loc['2017-01-01']
df_group = df.groupby(level=0)
mean = df_group.mean()
sum = df_group.sum()
count = df_group.count()
print "mean is :"
print mean
print "sum is :"
print sum
print "count is :"
print count







