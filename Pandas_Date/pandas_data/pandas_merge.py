# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np


df1 = pd.DataFrame({
                   "lkey": ['a', 'b', 'c', 'a'],
                   "key": ['one', 'two', 'one', 'two']
                   })

df2 = pd.DataFrame({
                   "rkey": ['a', 'b', 'd', 'd'],
                   "key": ['three', 'two', 'one', 'one']
                   })
# 默认how为inner，on为重合的列
print pd.merge(df1, df2)

print pd.merge(df1, df2, how="outer")

# 当没有重合的列时，通过left_on和right_on进行指定
print pd.merge(df1, df2, left_on="lkey", right_on="rkey")

# 当列名相同时，默认_x,_y区分，可以通过suffixes进行区分
print pd.merge(df1, df2, left_on="lkey", right_on="rkey", suffixes=('_left', '_right'))


# 若连接键位于索引中，使用left_index或者right_index
left = pd.DataFrame([[1, 2], [2, 3], [3, 4]], columns=["one", "two"], index=['a', 'b', 'c'])
right = pd.DataFrame([[1, 2, 3, 4], [2, 3, 6, 6], [3, 4, 7, 5], [3, 6, 8, 9]], columns=["first", "second", "third", 'fourth'],
                     index=['a', 'b', 'c', 'd'])

print ""
print pd.merge(left, right, left_index=True, right_index=True)


# 对于层次化索引
left = pd.DataFrame({'name': ["vic", "myw", "jd", "wyh"],
                     "year": [1995, 1996, 1995, 1994],
                     "age": [22, 21, 22, 23]}
                    )
right = pd.DataFrame(np.arange(12).reshape((6, 2)), columns=['event1', 'event2'],
                     index=[["vic", "jd", "zxy", 'wyh', 'gy', 'm'], [22, 21, 23, 33, 4, 33]])
print "left"
print left
print "right"
print right
print pd.merge(left, right, left_on=["name", "age"], right_index=True)


# merge和join的区别
# merge是以某一个相同的列开始，进行合并
# join默认是以索引进行合并



