# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from myproject.sql import session

from myproject.items import CommitItem
from myproject.sql import Agency


class ProvincePipeline1(object):

    def process_item(self, item, spider):
        if item['name']:
            return item
        else:
            raise DropItem("none item")


class ProvincePipeline2(object):

    def process_item(self, item, spider):
        print item['name']
        return item


class AgencyPipeline(object):

    def process_item(self, item, spider):
        if isinstance(item, CommitItem):
            session.commit()
        else:
            agency = Agency()
            agency['province'] = item['province']
            agency['city'] = item['city']
            agency['country'] = item['country']
            agency['address'] = item['address']
            agency['count'] = item['count']
            session.add(agency)


