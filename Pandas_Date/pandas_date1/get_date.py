# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np


long_date = pd.Series(np.random.rand(1000), index=pd.date_range("2017-01-01", periods=1000))

# print long_date
# # 只传入年
# print "只传入年："
# print long_date["2017"]

# 通过切片的方式获取数据
dates = pd.date_range("2017-01-01", periods=100)
test_date = pd.DataFrame(np.random.rand(100, 4), index=dates, columns=['m', 'y', 'w', 'v'])
print test_date
print test_date['2017-01']
print test_date['2017-01-01':'2017-01-07']






