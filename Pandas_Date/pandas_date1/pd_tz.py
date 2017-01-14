# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

#    世界的每个地区都有自己的本地时间，在Internet及无线电通信时，时间的统一非常重要！
#    整个地球分为二十四时区，每个时区都有自己的本地时间。
#    在国际无线电通信中，为统一而普遍使用一个标准时间，称为通用协调时(UTC, Universal Time Coordinated)。
#    UTC与格林尼治平均时(GMT, Greenwich Mean Time)一样，都与英国伦敦的本地时相同。UTC与GMT含义完全相同。


# 一旦本地化到特定的时区，就可以利用tz_convert转换到别的时区
# 可以直接对numpy或者pandas进行操作
dates = pd.date_range("2017-01-03 09:30", periods=10, freq="4h")  # 本地时间
print dates

dates_utc = dates.tz_localize("UTC")
print dates_utc

dates_us = dates_utc.tz_convert("US/Eastern")
print dates_us

print dates.tz_localize("US/Eastern").tz_convert("UTC")

