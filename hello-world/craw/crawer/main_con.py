#coding:utf-8
from crawer import url_open, html_parser, output
import time
class Mainfun(object):

    def __init__(self):
        self.url_open = url_open.Urlopen()
        self.html_parser = html_parser.Htmlparser()
        self.output = output.Output()

    def craw(self, enterurl):
        count = 1
        while True:
            html = self.url_open.open(enterurl)
            urls = self.html_parser.parse(enterurl,html)
            while self.html_parser.hasimage(urls):
                print 'Crawing NO.%d ' %count
                url = self.html_parser.getone(urls)
                html2 = self.url_open.open(url)
                image1 = self.html_parser.last(enterurl,html2)
                image = self.url_open.open(image1)

                self.output.output(count,image)
                time.sleep(2)
                #print data
                if count == 1000:
                    break
                count += 1
            if count == 1000:
                break


enterurl = 'http://alpha.wallhaven.cc/random'
spider = Mainfun()
spider.craw(enterurl)







