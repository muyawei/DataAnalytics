# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
dates = pd.date_range("2017-01-01", periods=10, freq="W")
df = pd.DataFrame(np.random.rand(10, 2), index=dates, columns=[1, 2])

print df
# 以固定的频率显示
df_resample = df.resample("D")
print df_resample
# 降采样
# 1。resample的相关参数
# 查看运行结果，即使是从02开始的，resample为5min，开始的为00：00：00
s = pd.Series(np.arange(14), index=pd.date_range("20170103 00:02:00", periods=14, freq="T"))
print s
s_default = s.resample("5min")
print s_default.sum()

s_left = s.resample("5min", closed="left", label="left")
print s_left.sum()

# ohlc -- open high low close
s_ohlc = s.resample("5min").ohlc()
print s_ohlc

# 2。通过groupby进行
dates = pd.date_range("20170101", periods=100, freq="D")
ss = pd.Series(np.arange(100), index=dates)
print ss.groupby(lambda a: a.month).sum()

# 升采样 (可能会出现空数据)
s = pd.Series(np.arange(14), index=pd.date_range("20170101", periods=14, freq="W"))
print s
s_grow = s.resample("D")
print s_grow.sum()
s.plot()





