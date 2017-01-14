# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
# 通过groupby进行分组，然后计算某一列的中位数
df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three']})
                   # 'C': np.random.randn(8),
                   # 'D': np.random.randn(8)})

print df
print "test"
print df.groupby(["A", "B"])['A', "B"].count()
print "对分组进行测试"
print df

print ""
print "获取分组后的全部数据:对于B列，因为为字符列，没有中位数，所以不会显示"
print df.groupby("A").size()

print ""
print "获取分组后的某一列数据：groupby里面不能只写A"
print df['C'].groupby([df['A'], df['B']]).max()
means = df['C'].groupby([df['A'], df['B']]).max()

print "语法糖"
print df.groupby('A')['C'].max()
print df.groupby('A')[['C']].max()

print ""
print "unstack"
print means.unstack()

print ""
print "实际上，分组键可以是任意长度适当的数组"
array1 = np.array(["ss", "as", 'aa', 'ss', 'aa', 'as', 'ss', 'sss'])
array2 = np.array(['ee', 'rr', 'ee', 'ee', 'ee', 'rr', 'r', 'e'])
print df["C"].groupby([array1, array2]).max()



print ""
print "对分组进行迭代"
for (name1, name2), group in df.groupby([df['A'], df['B']]):
    print name1, name2
    print group

