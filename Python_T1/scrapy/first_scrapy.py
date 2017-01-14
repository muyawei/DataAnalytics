# -*- coding:utf-8 -*-
import scrapy


class FirstSpider(scrapy.Spider):
    name = "First_spider"
    start_urls = ["http:www.baidu.com"]

    def parse(self, response):
        print "------------"
        print response.url
        print response.headers
        print response.body

