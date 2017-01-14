#coding=utf-8
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from pylab import mpl
from datetime import datetime, timedelta


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()-0.3, 1.03*height, '%s' % int(height), fontsize=10)
province_file_name = u'各省份订单金额%s.jpg' % "a"
region_file_name = u'各区订单金额%s.jpg' % "b"

station_total_fee_region = list()
zhong_to_pinyin = {u"东北区": "dongbei", u"华东A区": "huadongA", u"华东B区": "huadongB", u"华中区": "huazhong",
                   u"华北区": "huabei", u"华南区": "huanan", u"西南区": "xinan"}
total_fee_by_region = {u"东北区": "11", u"华东A区": "33", u"华东B区": "66", u"华中区": "11",
                       u"华北区": "22", u"华南区": "44", u"西南区": "55"}
for region, total_fee in total_fee_by_region.items():
    station_total_fee = dict()
    station_total_fee['region'] = zhong_to_pinyin[region]
    station_total_fee['total_fee'] = total_fee
    station_total_fee_region.append(station_total_fee)
print station_total_fee_region

mpl.rcParams['font.family'] = ['sans-serif']
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
p_values = "黑龙江".decode("utf-8")
station_total_fee = [{'province': u"东北区", 'total': 185704}, {'province': u'华北区', 'total': 185704},
                     {'province': u'华东A区', 'total': 223000}, {'province': u'华北区', 'total': 924500},
                     {'province': u'华南区', 'total': 134300}, {'province': u'东北区', 'total': 123444},
                     {'province': u'华东B区', 'total': 234700}, {'province': u"华东A区", 'total': 185704},
                     {'province': u'西南区', 'total': 185704}, {'province': u'华东B区', 'total': 924500},
                     {'province': u'华中区', 'total': 223000}, {'province': u'西南区', 'total': 924500},
                     {'province': u'华中区', 'total': 134300}, {'province': u'西南区', 'total': 123444},]
#查看两个问题：1.是否为unicode编码 2.是否为数字
station_total_fee_pinyin = list()
for province in station_total_fee:
    pinyin = dict()

# [{'province': u'\u9ed1\u9f99\u6c5f', 'total': '1000'}, {'province': u'\u5409\u6797', 'total': '1900'}, {'province': u'\u8fbd\u5b81', 'total': '2000'}, {'province': u'\u5317\u4eac', 'total': '900'}, {'province': u'\u4
plt.figure()
df1 = pd.DataFrame(station_total_fee)
x_len = len(station_total_fee)
x_narray = np.array(range(1, 2 * x_len, 2))
print x_narray
plt.xticks(x_narray, df1['province'].values, size='small', rotation=20)
width = 0.5
rect_total = plt.bar(x_narray, df1['total'].values, width, align="center", color='#00a1f2', label="total_original")
# rect_count = plt.bar(x_narray, df1['count'].values, width, align="center", color='g', label="total_original")
print (df1['total'].values.max()/1000+1.5)*1000
plt.axis([x_narray.min()-0.5, x_narray.max()+0.5, 0, (df1['total'].values.max()/100000+1.5)*100000])
plt.legend(loc='best')
yesterday_time = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
plt.title(yesterday_time+" "+u"各省油站交易量")
for a, b in zip(x_narray, df1['total'].values):
    plt.text(a, b*1.03, '%.2f' % b, ha='center', va='bottom', fontsize=8)
# autolabel(rect_total)
plt.savefig("a.jpg")


plt.show()
plt.figure()
df = pd.DataFrame(station_total_fee)
x = df['total'].values
labels = df['province'].values
colors = ['#69f200', '#00a1f2', '#fff500', '#f8c400', '#ff7f00', '#ff00fe', '#f22a1f']
# explode = [0.2, 0.1, 0, 0, 0.1, 0]
plt.pie(x, labels=labels, autopct='%1.1f%%', colors=colors)
plt.savefig("b.jpg")


plt.show()
