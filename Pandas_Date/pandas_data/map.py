# -*- coding:utf-8 -*-
import pandas as pd

df = pd.DataFrame({"name": ["myw", 'jd', 'gs', 'lxm'],
                   "city": ["sys", "Sys", "jgdq", "wh"]
                   })
city_to_province = {"sys": "H", "jgdq": "H", "wh": "S"}

df["province"] = df["city"].map(str.lower).map(city_to_province)
print df

df = pd.DataFrame([{"city": "sys", "_channel": "h", "sum": 100},
             {"city": "sys", "_channel": "h", "sum": 100},
             {"city": "wh", "_channel": "s", "sum": 100}])

city_to_province = {"sys": "H", "jgdq": "H", "wh": "S"}

df[u"省份"] = df["city"].map(city_to_province)
print df
df = df.groupby([u"省份", "_channel"])[['sum']].sum()

pf = pd.DataFrame(df)
p = pf.unstack(u"省份")
p.index.name = u"渠道"
#
# df = pd.DataFrame(city_channel)
# print df
# df[u"省份"] = df["city"].map(city_to_province)
# df = df.groupby([u"省份", "_channel"])['sum'].sum()
# df_oil = pd.DataFrame(df)
# df_oil = df_oil.unstack(u"省份")
# df_oil.index.name = u"渠道"

# columns_name = []
# for name in df_oil.columns.values:
#     columns_name.append(name[1])
# values = df_oil.values
# index_name = df_oil.index.values
#
# df_oil = pd.DataFrame(values, columns=columns_name, index=index_name)
# df_sum = df_oil.sum(axis=1)
# df_sum = pd.DataFrame(df_sum, columns=[u"总订单"])
# df_oil = df_oil.join(df_sum)


columns_name = []
for name in p.columns.values:
    columns_name.append(name[1])
values = p.values
index_name = p.index.values

df_oil = pd.DataFrame(values, columns=columns_name, index=index_name)

df_oil_sum = df_oil.sum(axis=1)
df_sum = pd.DataFrame(df_oil_sum, columns=[u"总订单"])
df_oil_sum = pd.merge(df_oil, df_sum, left_index=True, right_index=True)
print p