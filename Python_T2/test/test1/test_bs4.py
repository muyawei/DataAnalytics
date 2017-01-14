# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
html_doc = "<a href='123.html' class='article_link'> Python </a>"
soup = BeautifulSoup(html_doc, 'html.parser', from_encoding="utf-8")
nodes = soup.find_all('a', class_='article_link')
for node in nodes:
    print node.name, node['href'], node.get_text()

