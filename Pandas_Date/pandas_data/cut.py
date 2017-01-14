# coding:utf-8
import pandas as pd

# 将数据根据所给的区间进行切割,然后根据pd.value_counts进行分隔，哪边是闭端，可以通过ringht = False进行选择
ages = [22, 33, 44, 32, 42, 21, 56, 11, 65, 63, 21, 67, 99]
bin = [20, 40, 80, 100]
c = pd.cut(ages, bin)
print c
cnt = pd.value_counts(c)
print cnt

# 可以设置自己的面元名称
names = ["young", "middle", 'old']
c_name = pd.cut(ages, bin, labels=names)
print c_name
cnt = pd.value_counts(c_name)
print cnt


# 如果想cut传入的是面元的数量，而不是面元的数据，会自动分组(根据最大值和最小值)
c_auto = pd.cut(ages, 4, precision=2)
print c_auto
cnt = pd.value_counts(c_auto)
print cnt

# qcut 类似与cut，根据样本分位数对数据进行划分
q_auto = pd.qcut(ages, 4, precision=2)
print q_auto
cnt = pd.value_counts(q_auto)
print cnt

# qcut也可以自定义分位数******(0到1之间的数)
q_auto = pd.qcut(ages, [0, 0.3, 0.6])
print q_auto
cnt = pd.value_counts(q_auto)
print cnt



