# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

# 对之后或者超前的数据进行处理

df = pd.DataFrame(np.random.rand(3, 3), index=pd.date_range("20170103", periods=3), columns=np.arange(3))
print df
print df.shift(1)   # 单纯的位移操作不会影响索引，部分数据会丢失
print df.shift(1, freq="D")  # 添加频率，对时间戳进行位移



