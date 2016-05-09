#coding:utf-8
import time

from crawer_liao import url_open, html_parser1, output1, url_manager


class Mainfun(object):

    def __init__(self):
        self.url_open = url_open.Urlopen()
        self.html_parser = html_parser1.Htmlparser()
        self.output = output1.Output()
        self.url_manager = url_manager.Urlmanager()

    def craw(self, enterurl, homeurl):
        count = 1
        html = self.url_open.open(enterurl)
        urls = self.html_parser.parse(homeurl, html)
        while self.url_manager.notfinished(urls):

            print 'Crawing NO.%d ' %count
            url = self.url_manager.getone(urls)
            html2 = self.url_open.open(url)
            filename,dic = self.html_parser.last(html2)
            self.output.output(count ,filename, dic)

                #print data
            if count == 200:
                break
            count += 1



enterurl = 'http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000'
homeurl = 'http://www.liaoxuefeng.com'
spider = Mainfun()
spider.craw(enterurl,homeurl)







