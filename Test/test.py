# coding:utf-8
import pandas as pd
import datetime
test_list = [{"all": 22, "channel": "ios", "city": "hrb"},
             {"all": 32, "channel": "ios", "city": "bj"},
             {"all": 52, "channel": "ios", "city": "sd"},
             {"all": 22, "channel": "ios", "city": "dd"},
             {"all": 242, "channel": "ios", "city": "hb"},
             {"all": 22, "channel": "and", "city": "hrb"},
             {"all": 32, "channel": "and", "city": "bj"},
             {"all": 52, "channel": "and", "city": "sd"},
             {"all": 22, "channel": "and", "city": "dd"},
             {"all": 242, "channel": "and", "city": "hb"}
             ]

df = pd.DataFrame(test_list)
print df

df_real = df.pivot("channel", "city")
df_real[u"总订单"] = df_real.sum(axis=1, level=0)
df_real.index.name = u'渠道'
df_real.columns.name = u"省份"
print df_real
file_name = "aa"
with pd.ExcelWriter('oil.xls') as writer:
    df_real.to_excel(writer, sheet_name="a")






