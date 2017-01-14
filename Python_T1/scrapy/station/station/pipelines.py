# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from station.sql import session

from station.items import CommitItem
from station.sql import Station

class StationPipeline(object):
    def process_item(self, item, spider):

        if isinstance(item, CommitItem):
            session.commit()
        else:
            station = Station()
            station.bureau = item['bureau']
            station.state = item['state']
            station.name = item['name']
            station.address = item['address']
            station.passenger = item['passenger']
            station.luggage = item['luggage']
            station.package = item['package']
            session.add(station)