# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                   'C': np.arange(8),
                   'D': np.arange(8)})


# apply会将待处理的对象拆分成多个片段，然后对个片段调用传入的参数，最后尝试将各片段组合到一起
print df


# 获取C列数据最大的行
def top(df, column="C", num=1):
    return df.sort_values(by=column)[-num:]

print df.groupby("A")
print df.groupby("A").apply(top)

print df.groupby("B", group_keys=False).apply(top, column="D")
