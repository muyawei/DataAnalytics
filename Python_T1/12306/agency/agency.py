# -*- coding:utf-8 -*-
import requests
#import urllib3
import json
import time


# https://kyfw.12306.cn/otn/userCommon/allProvince  --allprovince
# {"validateMessagesShowId":"_validatorMessage","status":true,"httpstatus":200,
# "data":[{"chineseName":"安徽","allPin":"","simplePin":"ah","stationTelecode":"34"},
#         {"chineseName":"北京","allPin":"","simplePin":"bj","stationTelecode":"11"},
#        ...]
# https://kyfw.12306.cn/otn/queryAgencySellTicket/query?province=安徽&city=&county=
# 返回数据的结果
# {"validateMessagesShowId":"_validatorMessage","status":true,"httpstatus":200,
# "data":{"datas":[{"bureau_code":"G","station_telecode":"JJG","belong_station":"九江","province":"安徽","city_code":"","city":"安庆",
#                   "county":"宿松县","windows_quantity":"1","agency_name":"宿松县汇口镇代售点",
#                   "address":"安徽省宿松县汇口镇德化路64号","addressencode":"%B0%B2%BB%D5%CA%A1%CB%DE%CB%C9%CF%D8%BB%E3%BF%DA%D5%F2%B5%C2%BB%AF%C2%B764%BA%C5","phone_no":"0556-7580222","start_time_am":"0730","stop_time_am":"1200","start_time_pm":"1200","stop_time_pm":"1830"},
#                  {"bureau_code":"G","station_telecode":"JJG","belong_station":"九江","province":"安徽","city_code":"","city":"安庆",
#                   "county":"宿松县","windows_quantity":"1","agency_name":"宿松县宿松路代售点",
#                   "address":"安徽省宿松县孚玉镇宿松路211号（汽车站旁）","addressencode":"%B0%B2%BB%D5%CA%A1%CB%DE%CB%C9%CF%D8%E6%DA%D3%F1%D5%F2%CB%DE%CB%C9%C2%B7211%BA%C5%A3%A8%C6%FB%B3%B5%D5%BE%C5%D4%A3%A9","phone_no":"0556-7818730","start_time_am":"0800","stop_time_am":"1200","start_time_pm":"1400","stop_time_pm":"1830"},
#                   ...]}

def getProvince():

    s = requests.get("https://kyfw.12306.cn/otn/userCommon/allProvince", verify=False)

    # 返回的是json数据，所以不需要解析器进行解析，将它转化为json格式
    j = s.json()
    names = j['data']
    chineseName=[]
    for name in names:
        #print name['chineseName']
        chineseName.append(name['chineseName'])
    # print chineseName
    return chineseName



def getData(province):
    url = "https://kyfw.12306.cn/otn/queryAgencySellTicket/query"
    param = {"province": province, "city": "", "county": ""}
    ds = requests.get(url, params=param, verify=False)

    resp = ds.json()
    agencys = resp['data']['datas']
    out = ""
    for agency in agencys:
        out += agency['province'] + "\t"
        out += agency['city'] + "\t"
        out += agency['county'] + "\t"
        out += agency['windows_quantity'] + "\t"
        out += agency['agency_name'] + "\t"
        out += "\n"

    return out.encode("utf-8")

if __name__ =="__main__":
    #获取所有省份信息　
    provinces = getProvince()

    #根据省份信息获取所有的数据，并写入文件
    for i in range(0, len(provinces)):
        with open(provinces[i].encode("utf-8")+u".txt".encode("utf-8"), "w+") as f:
            f.write(getData(provinces[i]))
            print i
        time.sleep(5)

