# -*- coding:utf-8 -*-
import json

import scrapy
from scrapy import Request


class SingleCustom(scrapy.Spider):
    name = "single_custom"
    start_urls = ["https://www.baidu.com/s?wd=1"]

    custom_settings = {
        'DUPEFILTER_BEBUG': True,
        'DUPEFILTER_CLASS': "test_scrapy_exact.filters.CustomURLFilter.CustomURLFilter"
    }

    def parse_e(self, response):
        self.logger.info(response.url)
        self.logger.info(response.meta)

    def parse(self, response):
        self.logger.info("------------")
        yield Request(url="https://www.baidu.com/s?wd=1", callback=self.parse_e)
        yield Request(url="https://www.baidu.com/s?wd=3", callback=self.parse_e)
        yield Request(url="https://www.baidu.com/s?wd=3", callback=self.parse_e)
        yield Request(url="https://www.baidu.com/s?wd=3", callback=self.parse_e, meta={"timestamp": "1"})
        yield Request(url="https://www.baidu.com/s?wd=3", callback=self.parse_e, meta={"timestamp": "2"})
        yield Request(url="https://www.baidu.com/s?wd=3", callback=self.parse_e, meta={"timestamp": "2"})
