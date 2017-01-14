# coding:utf-8
import pandas as pd
import numpy as np

# 对数据进行随机排列
df = pd.DataFrame(np.random.rand(5, 4))
_index = np.random.permutation(5)
random_df = df.take(_index)
print df
print _index
print random_df

# 可以模拟随机抽样，直接舍去一部分数据(不会出现重复)
sub_random_df = df.take(np.random.permutation(len(df))[:3])
print sub_random_df


# 还可以使用randint(可能出现重复数据)
_np = np.arange(10)
rand_np = _np.take(np.random.randint(0, len(_np), size=len(_np)))
print _np
print rand_np


