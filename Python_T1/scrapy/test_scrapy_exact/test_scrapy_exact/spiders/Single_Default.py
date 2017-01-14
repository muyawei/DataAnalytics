# -*- coding:utf-8 -*-
import scrapy
from scrapy import Request


class Single_Default(scrapy.Spider):
    name = "single_default"
    start_urls = ["https://www.baidu.com/s?wd=22"]

    def parse_e(self, response):
        self.logger.info(response.url)
        yield Request(url=response.url, callback=self.parse_e)

    def parse(self, response):
        self.logger.info("----------")

        yield Request(url="https://www.baidu.com/s?wd=3&s=1", callback=self.parse_e)
        yield Request(url="https://www.baidu.com/s?wd=3&s=2", callback=self.parse_e)
