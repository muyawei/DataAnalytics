# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
# 用参数对象中的数据为调用者对象"打补丁"
df1 = pd.DataFrame({"a": [1, 3, np.NaN, 4],
                    "b": [2, np.NaN, 4, 6]
                    })

df2 = pd.DataFrame(np.arange(12).reshape((2, 6)))

df = df1.combine_first(df2)
print "df1"
print df1
print "df2"
print df2
print "df"
print df


df2 = pd.DataFrame(np.arange(12).reshape((6, 2)), columns=["a", "b"])
df = df1.combine_first(df2)
print "df1"
print df1
print "df2"
print df2
print "df"
print df
