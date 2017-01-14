# coding:utf-8
import pandas as pd
# 利用pandas进行文件的读取。
# 一般来说，对于文本中有逗号的文件，一般使用pd.read_csv来进行解析。
# 若是有read_table，需要使用sep，显示用逗号进行分隔

# 对于文本中不存在逗号，而是使用" "空格进行分隔的文件，一般使用sep="\s+"，进行匹配
print "read_cvs 默认分隔符为逗号"
pd_ex1 = pd.read_csv("ch06/ex1.csv")
print pd_ex1

print "read_table默认以制表符'\t'分隔"
pd_ex1_tab = pd.read_table("ch06/ex1.csv", sep=",")
print pd_ex1_tab

print "csv中只是数据没有header,设为None为默认值"
pd_ex2 = pd.read_csv("ch06/ex2.csv", header=None)
print pd_ex2

print '若想把其中的某一列数据转化为index列，使用index_col即可'
pd_ex2_names = pd.read_csv("ch06/ex2.csv", names=["a", "b", "c", "d", "message"], index_col="message")
print pd_ex2_names


pd_ex3 = pd.read_csv("ch06/ex3.csv", sep="\s+")
print pd_ex3

pd_ex3 = pd.read_table("ch06/ex3.csv", sep="\s+")
print pd_ex3

pd_ex3 = pd.read_table("ch06/ex3_test.csv", sep="\s+")
print pd_ex3

print "当某些行没有意义时"
pd_ex4 = pd.read_csv("ch06/ex4.csv")
print pd_ex4

pd_ex4 = pd.read_csv("ch06/ex4.csv", skiprows=[0, 2, 3], index_col="message")
print pd_ex4

print "对于NA值，设置某些字段为Na值"
pd_ex5 = pd.read_csv("ch06/ex5.csv")
print pd_ex5

na = {"message": ["world"], "something": "one"}
pd_ex5 = pd.read_csv("ch06/ex5.csv", na_values=na)
print pd_ex5

data = pd.read_csv("ch06/ex1.csv")
# 默认写到csv文件的分隔符为","
data.to_csv("test.csv")
data.to_csv("test_write.csv", sep="|", na_rep="null", index=False, header=False)









