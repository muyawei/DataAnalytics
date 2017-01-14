# -*- coding: utf-8 -*-
import re
import urlparse
from bs4 import BeautifulSoup


class HtmlParser(object):

    def parse(self, new_url, html_cont):
        if new_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding="utf-8")
        new_urls = self._get_new_urls(new_url, soup)
        new_data = self._get_new_data(new_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()

        links = soup.find_all("a", href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        new_datas = {}

        new_datas['url'] = page_url
        print "new_datas",new_datas
#       <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find("dd", class_="lemmaWgt-lemmaTitle-title").find("h1")
        print title_node
        new_datas['title'] = title_node.get_text()

#       <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find("div", class_='lemma-summary')
        new_datas['summary'] = summary_node.get_text()
        print "new_datas",new_datas
        return new_datas


