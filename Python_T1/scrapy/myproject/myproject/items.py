# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProvinceItem(scrapy.Item):
    name = scrapy.Field()


class AgencyItem(scrapy.Item):
    province = scrapy.Field()
    city = scrapy.Field()
    country = scrapy.Field()
    count = scrapy.Field()
    address = scrapy.Field()


class CommitItem(scrapy.Spider):
    pass




