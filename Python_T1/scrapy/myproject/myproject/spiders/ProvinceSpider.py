# -*- coding:utf-8 -*-
import scrapy
import json
from myproject.items import ProvinceItem


class ProvinceSpider(scrapy.Spider):
    name = "province spider"
    start_urls = ["https://kyfw.12306.cn/otn/userCommon/allProvince"]
    custom_settings = {
            'ITEM_PIPELINES': {
                 'myproject.pipelines.ProvincePipeline1': 300,
                 'myproject.pipelines.ProvincePipeline2': 400,

            }
    }
    def parse(self, response):
        j = json.loads(response.body)
        for data in j['data']:
            item = ProvinceItem()
            item['name'] = data["chineseName"]
            yield item

        item = ProvinceItem()
        item['name'] = None
        yield item


