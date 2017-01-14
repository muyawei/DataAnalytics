# -*-coding:utf-8 -*-
import pandas as pd
import numpy as np


p_date = pd.date_range('20160101', periods=6)
df = pd.DataFrame(data=np.random.rand(6, 5), index=p_date, columns=list('12345'))
print df

# 使用标签进行获取["相应的值"]---注意，是中括号[行，列]，一定是相应的数值，不能是分片的数字形式
# df.loc[0:2, 0:2]  不可以 ，需要改成df.loc['2016-01-01':'2016-01-03', '1':'3']
print df.loc['2016-01-01']

print df.loc[:, ['1', '2']]

# print df.loc[['2016-01-01', '2016-01-02'], '1':'3']  第一个用切片形式报错
print df.loc['2016-01-01': '2016-01-02', '1':'3']

print df.loc[p_date[0], '1']
print df.at[p_date[0], '1']

print df.loc['2016-01-01', '1']
# print df.at['2016-01-01', '1']  报错
#
#
#
#
# 　按位置进行选择
print '按位置进行选择'
print df.iloc[1]
print df.iloc[0:2, 0:2]
print df.iloc[[1, 2, 4], [1, 2]]
print df.iloc[1, 1]
print df.iat[1, 1]
#
#
#
#
#
# 布尔索引

p_date = pd.date_range('20160101', periods=6)
df = pd.DataFrame(data=np.random.randn(6, 5), index=p_date, columns=list('ABCDE'))
print df
# 全局选择，小于0的数据会被置为NaN
print df[df > 0]
# A大于0的行会被输出
print df[df.A > 0]

df['F'] = ['A', 'B', 'C', 'D', 'E', 'F']
print "F"
print df
print df[df['F'].isin(['A', 'B'])]


