# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

# wp = pd.Panel(np.random.randn(2, 5, 4), items=['Item1', 'Item2'], major_axis=pd.date_range('1/1/2000', periods=5),
#               minor_axis=['A', 'B', 'C', 'D'])
# print wp

# 有3个二维数组，2个一维数组，每个一维数组有两个数
# print np.random.randn(3, 2, 2)

s = pd.Series([1, 2, np.nan, 3], index=['A', 'B', "C", 'D'])
print s

df = pd.DataFrame(data=np.random.rand(2, 3), index=['a', 'b'], columns=['one', 'two', 'three'])
print df

# list为包含在一个引号当中，不可写多个,个数为列的个数
p_date = pd.date_range('20160101', periods=8)
df2 = pd.DataFrame(data=np.random.rand(8, 2), index=p_date, columns=list('12'))
print df2


df3 = pd.DataFrame({'A': 'one',
                    'B': pd.Series(1),
                    'C': np.array([3]),
                    'D': pd.Timestamp('20160101'),
                    'E': pd.Categorical(["test"])
                    })
print df3
print df3.dtypes

