#coding:utf-8
from NTU_crawer import url_man, url_open, html_parser, output

class Mainfun(object):

    def __init__(self):
        self.url_man = url_man.Urlman()
        self.url_open = url_open.Urlopen()
        self.html_parser = html_parser.Htmlparser()
        self.output = output.Output()

    def craw(self, original_url):
        count = 1
        self.url_man.addurl(original_url)
        while self.url_man.has_url() :
            try:
                newurl = self.url_man.getone()
                print 'Crawing NO.%d : %s' %(count, newurl)
                html = self.url_open.open(newurl)
                urls, datas = self.html_parser.parse(html, newurl)
                # print urls, datas
                self.url_man.addurls(urls)
                self.output.add(datas)
                #print data
                if count == 100 :
                    break
                count += 1
            except:
                print 'Failed'
        self.output.out_html()

originalurl = 'http://www.uestc.edu.cn'
spider = Mainfun()
spider.craw(originalurl)







