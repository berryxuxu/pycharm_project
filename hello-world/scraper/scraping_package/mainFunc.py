# -*- coding: UTF-8 -*-
from scraping_package import urlmanager
from scraping_package import html_downloader
from scraping_package import html_parser
from scraping_package import output

class spider1(object):
    def __init__(self):
        self.urls = urlmanager.UrlManager()
        self.downloader = html_downloader.Html_Downloader()
        self.parser = html_parser.Html_Parser()
        self.output = output.Output()

    def craw(self,entranceURL):
        count = 1
        self.urls.add_new_url(entranceURL)
        while self.urls.has_new_urls():
            try:
                new_url = self.urls.get_new_url()
                html_content = self.downloader.download(new_url)
                new_urls, new_datas = self.parser.parse(entranceURL,html_content)
                self.urls.add_new_urls(new_urls)
                print new_datas
                self.output.collect_data(new_datas)

                print 'now is NO.%d , %s' %(count, new_url)
                if count == 10:
                    break
                count += 1
            except:
                 print 'no page found'
        self.output.output_html()

entranceURL = 'http://baike.baidu.com/view/21087.htm'
obj_spider = spider1()
obj_spider.craw(entranceURL)