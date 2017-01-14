# -*-coding:utf-8 -*-
import numpy as np
import pandas as pd

p_date = pd.date_range('20160101', periods=6)
df = pd.DataFrame(data=np.random.randn(6, 5), index=p_date, columns=list('ABCDE'))

#重建索引允许更改/添加/删除指定轴索引,并返回数据副本
df2 = df.reindex(index=p_date[0:5], columns=list(df.columns)+['F'])
df2.iloc[0, 5] = 2
df2.iloc[1, 4] = np.nan
df2.iloc[2, 3] = np.nan
print df2

df3 = df2.copy()
df4 = df2.copy()
print df2.dropna(how='any')
print df3.fillna(value=5)
print pd.isnull(df4)

