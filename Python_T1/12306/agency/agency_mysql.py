# -*- coding:utf-8 -*-

import requests
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, INTEGER, String
import time
from sqlalchemy.orm import sessionmaker
engine = create_engine("mysql://root:123456@10.18.99.126:3306/test", echo=True)

# 获得Base
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Agency(Base):
    __tablename__ = "agency"
    id = Column(INTEGER, primary_key=True)
    province = Column(String(20))
    city = Column(String(20))
    country = Column(String(20))
    count = Column(INTEGER)
    address = Column(String(50))

Base.metadata.create_all(engine)


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
    agen = Agency()
    for agency in agencys:
        agen.province = agency['province']
        agen.city = agency['city']
        agen.country = agency['county']
        agen.count = agency['windows_quantity']
        agen.address = agency['agency_name']
        session.add(agen)
        session.commit()





if __name__ =="__main__":
    #获取所有省份信息　
    provinces = getProvince()

    #根据省份信息获取所有的数据，并写入文件
    for i in range(0, 2):
        getData(provinces[i])

        time.sleep(5)
