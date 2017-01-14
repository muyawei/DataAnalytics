# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StationItem(scrapy.Item):
    bureau = scrapy.Field()
    state = scrapy.Field()
    name = scrapy.Field()
    address = scrapy.Field()
    passenger = scrapy.Field()
    luggage = scrapy.Field()
    package = scrapy.Field()


class CommitItem(scrapy.Item):
    pass
