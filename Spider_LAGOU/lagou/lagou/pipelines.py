# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from items import CommitItem


class LagouPipeline(object):

    def process_item(self, item, spider):
        if isinstance(item, CommitItem):
            pass


