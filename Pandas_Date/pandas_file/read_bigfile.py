# coding:utf-8
import pandas as pd

df_ex6 = pd.read_csv("ch06/ex6.csv")
print df_ex6.groupby("key").count()

print "获取其中的前几行"
df_ex6 = pd.read_csv("ch06/ex6.csv", nrows=10)
print df_ex6

print "逐块读取文件，chunksize设置块数的大小,指的是每一块的行数，若为20，数据为100，则分为5块"
df_ex6 = pd.read_csv("ch06/ex6.csv", chunksize=20)
print "返回的是一个Textparser对象"
print df_ex6

# for chunk in df_ex6:
#     print chunk
#     print "----"


# *****注意：若之前使用过对chunk遍历过，在进行遍历得不到数据******
print "与之前的groupby等效的"
tot = pd.Series([])
for chunk in df_ex6:
    tot = tot.add(chunk["key"].value_counts(), fill_value=0)
print tot[:10]

df_ex6 = pd.read_csv("ch06/ex6.csv")
print df_ex6.groupby("key").count()[:10]