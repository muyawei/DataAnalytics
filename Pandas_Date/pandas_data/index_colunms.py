# coding:utf-8
import pandas as pd
import numpy as np
#  通过map或者rename将df的index和columns进行修改
#  rename还可以传入字典
#  若在其本身上修改则将inplace设为true

df = pd.DataFrame(np.random.rand(4, 4),
                  columns=["a", 'b', 'c', 'd'],
                  index=["one", "two", "three", "four"]
                  )
print df
df.index = ["q", "w", "e", "r"]
print "直接修改"
print df
print

df_index = df.index.map(str.upper)
df.index = df_index
print "通过map修改其格式，对于字符串操作比较简便"
print df
print

df.rename(columns=str.upper, index={"Q": "one"})
print "可以传入字典，对特定的名称进行修改"
print df
print

df.rename(columns=str.upper, index={"Q": "one"}, inplace=True)
print "inplace设为true，直接在df上进行修改"
print df
print






