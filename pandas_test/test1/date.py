# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
num = pd.date_range(end='20100110', periods=10)
num1 = pd.date_range('20100101', '20100601', freq='BM')
num2 = pd.date_range('00:00', '12:00', freq='1h20min')
print "num"
print num

print "num1"
print num1

print "num2"
print num2

# 指的是沿着时间轴将数据前移或后移。Series 和 DataFrame 都有一个 .shift() 方法用于执行单纯的移动操作，index 维持不变：
sh_date = pd.date_range("20160101", periods=6)
df = pd.DataFrame(data=np.random.rand(6), index=sh_date)
print "df"
print df

print "df.shift(2)"
print df.shift(2)

# 另一种移动方法是移动 index，而保持数据不变。这种移动方法需要额外提供一个 freq 参数来指定移动的频率：
# 每次数据加6天，每两天更新一次数据     df.shift(6, freq='2D') 更新增加的数据是6*2
print df
print df.shift(6, freq='2D')


print pd.date_range('2010-01', '2010-05', freq='M')
print pd.period_range('2010-01', '2010-05', freq='M')

p = pd.period_range('2010-01', '2010-05', freq='M')
p.asfreq('M', how='start')


