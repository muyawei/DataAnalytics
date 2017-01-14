# -*- coding:utf-8 -*-
import scrapy
from scrapy import Request


class Break(scrapy.Spider):
    name = "break"

    def start_requests(self):
        self.logger.info("---------start request")
        yield Request(url="https://www.baidu.com/s?wd=22")

    def parse_e(self, response):
        self.logger.info(response.url)
        yield Request(url=response.url + "_1", callback=self.parse_e)

    def parse(self, response):
        self.logger.info("----------")

        yield Request(url="https://www.baidu.com/s?wd=3&s=1", callback=self.parse_e)
        yield Request(url="https://www.baidu.com/s?wd=3&s=2", callback=self.parse_e)
