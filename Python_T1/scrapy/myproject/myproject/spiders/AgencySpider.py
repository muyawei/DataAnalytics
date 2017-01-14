# -*- coding:utf-8 -*-
# scrapy crawl "agencyspider"
import urllib

import scrapy
import json

from scrapy import Request

from myproject.items import AgencyItem

from myproject.items import CommitItem


class AgencySpider(scrapy.Spider):
    name = "agencyspider"
    start_urls = ["https://kyfw.12306.cn/otn/userCommon/allProvince"]
    custom_settings = {
        'ITEM_PIPELINES': {
            'myproject.pipelines.AgencyPipeline': 300

        }
    }

    def parse(self, response):
        url = "https://kyfw.12306.cn/otn/queryAgencySellTicket/query"
        j = json.loads(response.body)
        provs = j['data']

        for prov in provs:
            param = {"province": prov, "city": "", "county": ""}
            s_url = url +urllib.urlencode(param)
            # param = u"?province=" + prov + u"&city=" + "" + u"&county="+""
            print s_url
            yield Request(s_url, callback=self.parse_agency)

    def parse_agency(self, response):
        datas = json.loads(response.body)
        for data in datas["data"]["datas"]:
            item = AgencyItem()
            item['province'] = data["province"]
            item['city'] = data['city']
            item['country'] = data['country']
            item['address'] = data['address']
            item['count'] = data['windows_quantity']
            yield item
        yield CommitItem()
