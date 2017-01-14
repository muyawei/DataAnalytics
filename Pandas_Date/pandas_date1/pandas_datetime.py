# -*-coding:utf-8 *-*
import pandas as pd
import numpy as np


# pd.to_datetime将字符串类型的日期转化为datetime类型 或者 pd.DatetimeIndex
p_date = pd.date_range('20160101', periods=8)
pd_date = ['2016/02/3 01:22:33', '2022-3-3']
print p_date
df2 = pd.DataFrame(data=np.random.rand(8, 2), index=p_date, columns=list('12'))
print df2
date = pd.to_datetime(pd_date)
date1 = pd.DatetimeIndex(pd_date)
print date1

date_None = pd.to_datetime(pd_date + [None])
print date_None   # NaT 是pandas中时间戳数据NA的值

print date_None[1]
print pd.isnull(date_None)


# 时间序列
# ts.index DatetimeIndex
# tt.index RangeIndex
dates = pd.date_range("2017-01-01", periods=7)
ts = pd.Series(np.random.rand(7), index=dates)
print ts
print ts.index

tt = pd.Series(np.random.rand(7))
print tt
print tt.index


