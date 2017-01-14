# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np


# period 表示的是时间区间，比如数日，数月，数季，数年等
# 没太弄明白和datetime的区别在哪
ts = pd.Series(np.random.randn(5), index=pd.period_range('201001', '201005', freq='M'))
ts_start = ts.to_timestamp(how="start")
ts_end = ts.to_timestamp(how="end")
print ts
print ts_start
print ts_end
print ts_start.to_period()
print ts_end.to_period("M")


