# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PythonItem(scrapy.Item):
    companyShortName = scrapy.Field()
    salary = scrapy.Field()
    companyFullName = scrapy.Field()
    companyLabelList = scrapy.Field()


class CommitItem(scrapy.Item):
    pass


class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
