# -*-coding:utf-8 -*-
import pandas as pd
import numpy as np

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})

df_grouped = df.groupby("A")
# 对一列数据求多个值
print df_grouped['C'].agg(['max', 'min'])

# 对多列求值
print df_grouped['C', 'D'].agg(['max', 'min'])

# 对数据进行重命名  ---元组
functions = [("最大值", "max"), ("最小值", "min")]
print df_grouped['C', "D"].agg(functions)

# 对多列求值，每一类列求不同的值
print df_grouped.agg({"C": ["min", 'max'],
                      "D": ["min"]
                      })

# 综合
print df_grouped.agg({"C": functions,
                      "D": ["min"]
                      })



