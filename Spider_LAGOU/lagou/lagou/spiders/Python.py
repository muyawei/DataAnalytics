# -*- coding:utf-8 -*-
import scrapy
from scrapy import Request
from scrapy import FormRequest
import json
from items import PythonItem, CommitItem


class Python(scrapy.Spider):
    name = "python_salary"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
        "Connection": "keep-alive",
        "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Referer": "https://www.lagou.com/"
    }


def start_requests(self):
        url = "https://www.lagou.com/jobs/positionAjax.json?city=北京&first=true&pn=1&kd=Python"
        yield Request(url, callback=self.getData)

    # def parse(self, response):
    #     yield FormRequest.from_response(response, headers=self.headers,
    #                                     formdata={
    #                                         'first': 'true',
    #                                         'pn': '1',
    #                                         'kd': 'Python'
    #                                         },
    #                                     callback=self.getData)


def getData(self, response):
        #获取第一页的数据

    data = json.loads(response.body)
    pageNo = data['content']['pageNo']
    if pageNo < 30:
        pageNo += 1
    else:
        yield CommitItem()
    url = "https://www.lagou.com/jobs/positionAjax.json?city=北京&first=false&pn="+str(pageNo)+"&kd=Python"
    print "===========", data
    f_pageSize = data['content']['pageSize']
    for i in range(0, f_pageSize):
        item = PythonItem()
        results = data['content']['positionResult']['result']
        result = results[i]
        item['companyShortName'] = result["companyShortName"]
        item['salary'] = result["salary"]
        item['companyFullName'] = result["companyFullName"]
        item['companyLabelList'] = result["companyLabelList"]
        yield item
    yield Request(url, callback=self.getData)

