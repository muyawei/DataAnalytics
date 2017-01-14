# -*-coding:utf-8 -*-
import pandas as pd
import numpy as np


people = pd.DataFrame(np.random.rand(5, 5), columns=['a', 'b', 'c', 'd', 'e'], index=['vic', 'myw', 'jd', 'sy', 'yyqx'])


# 通过字典进行分组
print "通过字典进行分组"
mapping = {"a": "red", "b": "red", "c": "blue", "d": "red", "e": "blue"}
print people.groupby(mapping, axis=1).count()

print ""
print "通过函数进行分组"
# 通过函数进行分组
print people.groupby(len).count()

# 将函数与数组，列表，元组等混合使用
print ""
print "将函数与数组，列表，元组等混合使用"
key_list = ['one', 'one', 'one', 'two', 'two']
print people.groupby([len, key_list]).count()

# 根据索引级别分组
print ""
print "根据索引级别分组"
columns = pd.MultiIndex.from_arrays([['US', 'US', 'US', 'JP', 'JP'], [1, 3, 5, 1, 5]], names=['cty', 'num'])
df = pd.DataFrame(np.random.rand(5, 5), columns=columns)
print df.groupby(level='cty', axis=1).count()


