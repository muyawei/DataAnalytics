# -*- coding:utf-8 -*-
import scrapy

class StationSpider(scrapy.Spider):
    name = "stationspider"
    custom_settings = {
        "ITEM_PIPELINES": {
            ''
        }
                       }

    def start_requests(self):
        url = "https://kyfw.12306.cn/otn/queryTrainInfo/getTrainName?"

        t = (datetime.datatime.now() + datetime.timrdelta(days=3)).strftime("%Y-%m%d")
        params = {"date": t}

        s_url = url + urllib.urlencode(params)
        self.logger.debug("start url" + s_url)
        yield Request(s_url, callback=self.parse, meta={"t": t})


