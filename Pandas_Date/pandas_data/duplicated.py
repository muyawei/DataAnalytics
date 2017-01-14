# -*- coding:utf-8 -*-
import pandas as pd

df = pd.DataFrame({"one": [1, 1, 2, 1, 2, 3, 4],
                   "two": [1, 1, 4, 1, 3, 5, 6]
                   })
print df
print "判断各行是否是重复行，默认保留第一个重复值"
print df.duplicated()

print "判断各行是否是重复行，设置保留最后一个值"
print df.duplicated(keep="last")
print "去除重复的行"
print df.drop_duplicates()
print "以one为索引，去除重复的行"
print df.drop_duplicates(["one"])
