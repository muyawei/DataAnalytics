# -*- coding:utf-8 -*-
# from spiders.Single_Default import Single_Default
# from spiders.MiddleSpider import MiddleSpider

from spiders.Python import Python
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

crawler = CrawlerProcess(settings)


@defer.inlineCallbacks
def crawl():
    yield crawler.crawl(Python)


crawl()
crawler.start()