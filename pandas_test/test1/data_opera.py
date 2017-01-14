# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

# list为包含在一个引号当中，不可写多个,个数为列的个数
p_date = pd.date_range('20160101', periods=6)
df2 = pd.DataFrame(data=np.random.rand(6, 2), index=p_date, columns=list('12'))
print df2

# 　head(-1) 返回的是从头到倒数第一条数据
#   tail(-1) 返回的是从尾巴数开始截止到倒数第一条数据
# 　head(2) 返回的是从头数2条数据
#   tail(3) 返回的是从尾巴数开始3条数据
print "df2.head(2)"
print df2.head(2)
print 'df2.head(-1)'
print df2.head(-1)
print 'df2.tail(-1)'
print df2.tail(-1)
print 'df2.tail(3)'
print df2.tail(3)

# 计算每一列的相关数据
print 'df2.describe()'
print df2.describe()

print "数据倒转"
print df2.T

print "数据排序,以轴排序"
print df2.sort_index(axis=1)

print "数据排序，以值排序"
print df2.sort(columns="1")


