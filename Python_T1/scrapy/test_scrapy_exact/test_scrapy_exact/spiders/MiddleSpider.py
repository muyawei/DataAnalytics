# -*-coding:utf-8 -*-

import scrapy
from scrapy.http.request import Request
import datetime


class MiddleSpider(scrapy.Spider):
    name = 'middle'

    custom_settings = {
        'DUPEFILTER_DEBUG': True,
        'DOWNLOADER_MIDDLEWARES': {
            'test_scrapy_exact.middles.CustomDownloaderMiddleware.CustomDownloaderMiddleware': 500,
        }
    }

    def start_requests(self):
        self.logger.info("------------start requests")

        yield Request(url="https://www.baidu.com/s?wd=20")

    def parse_e(self, response):
        self.logger.info("-------------response")
        self.logger.info(response.url)

        yield Request(url="https://www.baidu.com/s?wd=1", callback=self.parse_e,
                      meta={"expire": response.meta['expire']})

    def parse(self, response):
        self.logger.info("--------------response 4 start")

        yield Request(url="https://www.baidu.com/s?wd=2", callback=self.parse_e,
                      meta={"expire": datetime.datetime.now() + datetime.timedelta(seconds=2)})

        yield Request(url="https://www.baidu.com/s?wd=3", callback=self.parse_e,
                      meta={"expire": datetime.datetime.now() + datetime.timedelta(seconds=2)})

        yield Request(url="https://www.baidu.com/s?wd=4", callback=self.parse_e,
                      meta={"expire": datetime.datetime.now() + datetime.timedelta(seconds=2)})
