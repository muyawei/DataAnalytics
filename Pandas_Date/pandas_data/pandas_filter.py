# coding:utf-8
import pandas as pd
import numpy as np
# 检测和过滤异常值，就是将异常值找出来，对其进行处理

np.random.seed(12345)
data = pd.DataFrame(np.random.randn(100, 4))
print data
print data.describe()
# 对于绝对值大于1的数，将其视为异常值
# 将其转化为1 或 -1
# np.sign返回由 1 和 -1组成的数组，表示原始值的符号
data[np.abs(data) > 1] = np.sign(data) * 1
print data
print data.describe()

