# coding:utf-8
import pandas as pd
import numpy as np
# 如果dataframe的某一列有k个不同的值，则可以派生出一个k列矩阵或dataframe（其值全为1或0）

df = pd.DataFrame({"key1": ["a", 'b', "a", "a", "c", "b"],
                   "key2": [1, 3, 4, 5, 6, 7]
                   })
print df

dump_df = pd.get_dummies(df["key1"], prefix="dump_")
print dump_df

# 结合原来的数据
df_with_dump = df[["key2"]].join(dump_df)
print df_with_dump

# 对比df["key"]和df[["key"]]
print df["key1"]
print df[["key1"]]

# 对它进行应用
# 从文件中获取数据
columns_name = ["id", "title", "type"]
movies = pd.read_table("movielens/movies.dat", sep="::", names=columns_name)
print movies
# 获取其中的标签信息  <generator object <genexpr> at 0x1044ddbe0>
type_gener = (set(type.split("|")) for type in movies["type"])
types = sorted(set.union(*type_gener))
print type_gener
print types

# 将其转化为dump格式(里面的types是sorted格式的)
dummy_type = pd.get_dummies(types, prefix="type")
print dummy_type

dummy_movies = pd.DataFrame(np.zeros((len(movies), len(types))), columns=types)
for i, type in enumerate(movies["type"]):
    dummy_movies.ix[i, type.split("|")] = 1
all = movies.join(dummy_movies.add_prefix("type_"))
print all