# -*- coding: UTF-8 -*-
import urlparse
from bs4 import BeautifulSoup
import re

class Html_Parser(object):
    def __init__(self):
        pass
    # <a target="_blank" href="/view/125370.htm">面向对象</a>
    def geturl(self, entrance_url, soup):
        url_set = set()
        for link in soup.find_all('a', href= re.compile('/view/\d+\.htm')):
            url = urlparse.urljoin(entrance_url, link['href'])
            url_set.add(url)
        return url_set

    def getdata(self, entrance_url, soup):
        dic = {}
        dic['url'] = entrance_url
        # <dd class="lemmaWgt-lemmaTitle-title">
        # <h1>Python</h1>
        title = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        dic['title']=title.get_text()
        # <div class="lemma-summary" label-module="lemmaSummary">
        summary = soup.find('div',class_="lemma-summary")
        dic['summary']=summary.get_text()
        return dic

    def parse(self, entrance_url, html_content):
        if entrance_url == None or html_content == None:
            return
        else:
            soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
            urls = self.geturl(entrance_url, soup)
            datas = self.getdata(entrance_url, soup)
            return urls, datas

