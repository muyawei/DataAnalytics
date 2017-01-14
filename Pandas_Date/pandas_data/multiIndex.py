# coding:utf-8
import pandas as pd
import numpy as np

multi_series = pd.Series(np.arange(6), index=([
    [u"橘子", u"橘子", u"苹果", u"梨", u"梨", u"柚子"],
    ["good", "bad", "good", "good", "good", "bad"]]))

print multi_series


multi_dataframe = pd.DataFrame(np.arange(12).reshape(4, 3),
                               index=[[u"苹果", u"苹果", u"橘子", u"梨"],
                                      [u"大", u"小", u"大" ,u"大"]
                                      ],
                               columns=[[u"价格", u"价格", u"产地"],
                                        [u"数量", u"数量", u"数量"]
                                        ]
                               )
print multi_dataframe
# 对层次化进行调换位置
swap = multi_dataframe.swaplevel(0, 1)
print swap

# 根据指定索引进行排序
sort = swap.sortlevel(0)
print sort

multi_dataframe.index.names = ["size", "type"]
multi_dataframe.columns.names = ["etc", "count"]

# 根据级别进行汇总(就是将代表的数据汇总)
print multi_dataframe
print multi_dataframe.sum(level="size")
print multi_dataframe.sum(level="etc", axis=1)
