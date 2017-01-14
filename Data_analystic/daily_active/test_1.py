# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 假数据
# data_and = [{"date": '12-09', "sum": 100}, {"date": '12-10', "sum": 134}, {"date": '12-11', "sum": 133}]
# data_ios = [{"date": '12-09', "sum": 200}, {"date": '12-10', "sum": 334}, {"date": '12-11', "sum": 233}]
# data_small = [{"date": '12-09', "sum": 197}, {"date": '12-10', "sum": 137}, {"date": '12-11', "sum": 153}]
#
# df_and = pd.DataFrame(data_and)
# df_ios = pd.DataFrame(data_ios)
# df_small = pd.DataFrame(data_small)
#
# data_sum_and = df_and['sum'].values
# print data_sum_and
# data_sum_ios = df_ios['sum'].values
# data_sum_small = df_small['sum'].values
# data_sum = data_sum_and + data_sum_ios + data_sum_small
# data_date = df_and['date'].values
#
# plt.xticks([0, 1, 2],
#            ["12-09", "12-10", "12-11"]
#            )
# plt.bar([0, 1, 2], data_sum_and, width=0.1, align="center", color='g', label="android")
# plt.bar([0, 1, 2], data_sum_ios, bottom=data_sum_and, width=0.1, align="center", color='b', label='ios')
# plt.bar([0, 1, 2], data_sum_small, bottom=data_sum_ios+data_sum_and,
#  width=0.1, align="center", color='y', label=u"小版本")
# plt.plot([0, 1, 2], data_sum, color='r', label="sum")
# plt.legend(loc='best')
# plt.title(u"日活走势站内")
# plt.show()


# cnt_sum = query_daily_active_cnt(activate_time, month_time)
# cnt_and = query_active_by_app(activate_time, month_time, 'cn.buding.martin')
# cnt_ios = query_active_by_app(activate_time, month_time, 'AstonMartin')



#
# 实际数据
# cnt_sum = [122, 99, 555, 666, 220, 333, 444,]
# cnt_and = [22, 33, 44, 55, 56, 76, 54]
# cnt_ios = [33, 45, 66, 33, 22, 55, 33]
#
# df = pd.DataFrame([cnt_sum, cnt_and, cnt_ios], index=['sum', 'and', 'ios'])
# df_reve = df.T
# data_sum_and = df_reve['and'].values
# data_sum_ios = df_reve['ios'].values
# data_sum = df_reve['sum'].values
# data_sum_small = data_sum - data_sum_and - data_sum_ios
# print data_sum_and
# print data_sum_ios
# print data_sum_small
# x_index = range(1, 8)
# date = list()
# for i in range(7, 0, -1):
#     date.append((datetime.now() - timedelta(days=i)).strftime("%m-%d"))
#
# print date
#
# plt.xticks(x_index, date)
#
# plt.bar(x_index, data_sum_and, width=0.2, align="center", color='#41baf2', label="android")
# plt.bar(x_index, data_sum_ios, bottom=data_sum_and, width=0.2, align="center", color='#4ce6fe', label='ios')
# plt.bar(x_index, data_sum_small, bottom=data_sum_ios+data_sum_and, width=0.2,
# align="center", color='#c3fef0', label=u"小版本")
# plt.plot(x_index, data_sum, color='r', label="sum")
# plt.legend(loc='best')
# plt.title(u"日活走势站内")
# plt.savefig(u'日活%s'% datetime.now().strftime("%m-%d"))
# plt.show()

# 表格练习
# cnt_sum = [122, 99, 555, 666, 220, 333, 444]
# cnt_and = [22, 33, 44, 55, 56, 76, 54]
# cnt_ios = [33, 45, 66, 33, 22, 55, 33]
#
# df = pd.DataFrame([cnt_sum, cnt_and, cnt_ios], index=['sum', 'and', 'ios'])
# df_reve = df.T
#
# with pd.ExcelWriter('news.xls') as writer:
#     df_reve.to_excel(writer, sheet_name=str(0))
#     df.to_excel(writer, sheet_name=str(1))

df0 = pd.read_excel('ad_user.xlsx', sheetname="android10d")
df1 = pd.read_excel('ad_user.xlsx', sheetname="iphone10d")
# print df0
# print df1
ids1 = list()
ids2 = list()
print df0[['id']][(df0.create_time >= '2016-12-22T00:00:00') & (df0.create_time < '2016-12-23T00:00:00')]

df_and = df0[['id']][(df0.create_time > '2016-12-22T00:00:00') & (df0.create_time < '2016-12-23T00:00:00')]
for id in df_and['id'].values:
     ids1.append(id)

df_iphone = df1[['id']][(df1.create_time > '2016-12-22T00:00:00') & (df1.create_time < '2016-12-23T00:00:00')]
for id in df_iphone['id'].values:
     ids2.append(id)
print len(ids1)
print len(ids2)

with open("android10d.txt", "w") as f:
    for id in ids1:
        f.write(str(id))
        f.write(",")


with open("iphone10d.txt", "w") as f:
    for id in ids2:
        f.write(str(id))
        f.write(",")
ids3 = list()
ids4 = list()

with open("android10d.txt", 'r') as f:
    ids3 = f.read().split(",")
    print ids3
    print len(ids3)

with open("iphone10d.txt", 'r') as f:
    ids4 = f.read().split(",")
    print ids4
    print len(ids4)

# # 添加新的列（列名）直接df若没有自动添加，添加新的行，要使用append
# print df0
# df0['small'] = df0['sum'] - df0['and'] - df0['ios']
#
# print df0
# print df0['small'].sum()
# sum_row = df0[['sum', 'and', 'ios', 'small']].sum()
# print sum_row
# row = pd.DataFrame(sum_row).T
# print row
# row.reindex(columns=df0.index)
# df0.append(row, ignore_index=True)  # 直接添加没用，要赋值给一个对象
# df1 = df0.append(row, ignore_index=True)  # 直接添加没用，要赋值给一个对象
# print df1.rename(index={7: 'sum'})
# print df1
l = ['222591265', '213150578']
ll = list()
for i in l:
    ll.append(long(i))
print ll
if 222591265 in ll:
    print "true"
else:
    print "false"



