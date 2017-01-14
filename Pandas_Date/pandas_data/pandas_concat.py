# -*-coding:utf-8 -*-
import pandas as pd
import numpy as np


s1 = pd.Series([1, 2], index=["a", "b"])
s2 = pd.Series([3, 4], index=["c", "d"])
s3 = pd.Series([5, 6], index=["e", "f"])
# 默认axis = 0
print pd.concat([s1, s2, s3])

# 列上合并
print "axis = 1"
print pd.concat([s1, s2, s3], axis=1)

print "创建一个层次化索引"
print pd.concat([s1, s2, s3], keys=["group1", 'group2', 'group3'])

print "指定在特定轴上的索引"
print pd.concat([s1, s2, s3], axis=1, join_axes=[["a", 'c', 'm']])

print "忽略无用index,不再使用原来的行索引，而是重新开始创建"
print pd.concat([s1, s2, s3], ignore_index=True)




