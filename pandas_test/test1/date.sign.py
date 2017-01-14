# -*-coding:utf-8 -*-
import pandas as pd
import numpy as np

p_date = pd.date_range('20160101', periods=6)
df = pd.DataFrame(data=np.random.randn(6, 5), index=p_date, columns=list('ABCDE'))

# 赋值一个新列，通过索引自动对齐数据
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20160102', periods=6))
df['F'] = s1

df.at[p_date[0], 'A'] = 0
df.iat[0, 1] = 0

df.loc[:, 'D'] = 5

df[df > 0] = -df
print df
