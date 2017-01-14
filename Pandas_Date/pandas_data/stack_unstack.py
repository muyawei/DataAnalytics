# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np


df = pd.DataFrame(np.arange(6).reshape((2, 3)),
                  columns=pd.Index(['one', 'two', 'three'], name="english"),
                  index=pd.Index(["第一", "第二"], name="chinese")
                  )

print df
print "stack 将列转化为行"
result = df.stack()
print result

print "unstack 将行转化为列(注意：对于一个层次化的索引，unstack将行转化为列)"
print result.unstack()

print "默认stack是最内层的，传入分层级别编号或名称，即可对其他级别进行转化"
print result.unstack(0)
print result.unstack("chinese")


print "如果不是所有级别值都能在分组中找到的话，unstack操作可能会引发缺失值"
s1 = pd.Series(np.arange(5), index=["a", 'b', 'c', 'd', 'e'])
s2 = pd.Series(np.arange(3), index=['d', 'e', 'f'])

df = pd.concat([s1, s2], keys=["one", 'two'])
print df
print "unstack"
result = df.unstack()
print df.unstack()

print "stack默认会过滤缺失值，该操作是可逆的"
print result.stack()

