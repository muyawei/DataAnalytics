# -*-coding:utf-8 -*-
import pandas as pd

df = pd.DataFrame({"city": ["hrb", "hrb", "bj", "bj"],
                   "item": ["apple", "pear", 'apple', 'pear'],
                   "value": ['2', '3', '4', '5'],
                   "number": ['100', '200', '300', '400']
                   })

print df
print "df类似于从数据库中获取的数据"

print "进行处理,一个转化为行，一个转化为列,值可选，默认为全部"
print df.pivot("city", "item")

print df.pivot(index="city", columns="item", values="value")
print "等价于"
normal = df.pivot("city", "item")
print normal['value']

# 另一种处理数据列转行的方法,将一个或多个列转化为行索引
# 与pivot的区别是，pivot会把以组数据转化为header的形式，
# 而set_index只是把数据转化为行索引
set_df = df.set_index(keys=["city", "item"])
print set_df
df = set_df.reset_index()
print df
