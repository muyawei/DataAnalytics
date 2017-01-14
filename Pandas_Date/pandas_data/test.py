# coding:utf-8
import pandas as pd
from datetime import date, timedelta, datetime


#
# s = [{u"累计":22,"_channel":"ios"}, {u"累计":22,"_channel":"360"}]
# df2 = pd.DataFrame(s)
# print df
# d = pd.merge(df1, df2, left_index=True, right_on="_channel", how="outer")
# d= d.reindex(columns=["_channel", u"总量",u"微信",u"累计"])
# print d


def save_file(start_time, end_time, file_name):
    channel_day = {"ios": 20, "android": 20}
    channel_weixin = {"apple": 20, "360": 20}
    s1 = pd.Series(channel_day)
    s2 = pd.Series(channel_weixin)

    df = pd.concat([s1, s2], axis=1)
    df = df.fillna(value=0)
    df1 = pd.DataFrame(df.values, columns=[u"总量", u"微信"], index=df.index)
    writer = pd.ExcelWriter(file_name)
    for i in range((end_time - start_time).days + 1):
        print i
        end = start_time + timedelta(days=i)
        start = end - timedelta(days=1)

        s = [{u"累计": 22, "_channel": "ios"}, {u"累计": 22, "_channel": "360"}]
        df2 = pd.DataFrame(s)

        d = pd.merge(df1, df2, left_index=True, right_on="_channel",
                     how="outer")
        d = d.reindex(columns=["_channel", u"总量", u"微信", u"累计"])
        sheet_name_oil = str(start)+u"加油统计"
        sheet_name_register = str(start)+u"注册数据"
        df1.to_excel(writer, sheet_name=sheet_name_oil, header=["a", 'b'])
        d.to_excel(writer, sheet_name=sheet_name_register)
    writer.close()

if __name__ == "__main__":
    start_time = date(2016, 11, 1)
    end_time = date(2016, 11, 2)
    import uuid
    filename = uuid.uuid4().hex + "multsheet.xls"
    save_file(start_time, end_time, filename)


# brand_model = {"huawei": {"model1": {"count": 20}, "model2": {"count": 10}},
#                "ios": {"4s": {"count": 20}, "5s": {"count": 10}}
#                }
# sum = 100
# for brand, model_dict in brand_model.items():
#     for model in model_dict:
#         print model
#         brand_model[brand][model][u"percent"] = \
#             brand_model[brand][model]["count"]/float(sum)*100
# print brand_model
#
# brand = {"huawei": {"count":20}, "xiaomi":{"count":10}}
# sum = 100
#
# for _brand, count in brand.items():
#     brand[_brand][u"percent"] = brand[_brand]["count"]/float(sum) *100
# print brand
#
# # 品牌
# df_brand = pd.DataFrame(brand)
# df_brand = df_brand.T
# print df_brand
#
#
# # **********多层set转化为dataframe***********
# piece =[]
# keys = []
# for brand, model_dict in brand_model.items():
#     df = pd.DataFrame(model_dict)
#     print "df", df.T
#     keys.append(brand)
#     piece.append(df.T)
#
# df_brand_model= pd.concat(piece, keys=keys)
# print df_brand_model
#
# with pd.ExcelWriter("a.xls") as writer:
#     df_brand.to_excel(writer, sheet_name=u"品牌")
#     df_brand_model.to_excel(writer, sheet_name=u"品牌——型号")
