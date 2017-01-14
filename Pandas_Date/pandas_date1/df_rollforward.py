# -*-coding:utf-8 -*-
import pandas as pd
import numpy as np
from pandas.tseries.offsets import MonthEnd


# 利用前滚，后滚和group_by结合,对日期进行分月group_by，进行mean，sum等数据的计算
offset = MonthEnd()   # 到达月末的数据，在rseries.offsets中还有好多偏移的锚点，可以进行计算
df = pd.DataFrame(np.random.rand(9, 3), index=pd.date_range("20170103", periods=9, freq="7D"))
print df
print "利用月进行分组,求其sum值:"
print df.groupby(offset.rollforward).sum()

print "进行分组，求相关数据更快捷的方式:"
print df.resample("M").sum()

