from bs4 import BeautifulSoup
import re
import urlparse

class Htmlparser(object):

    def _geturls(self, soup, original_url):
        urls = set()
        if soup.find('body').findAll('a') == None :
            print 'NO link'
            return
        links = soup.find('body').findAll('a', href=re.compile('^http://'))
        for link in links:
            if 'href' in link.attrs:
                #print link['href']
                #url = urlparse.urljoin(original_url, link['href'])
                url = link['href']
                urls.add(url)
        #print self.urls
        return urls

    def _getdatas(self, soup, original_url):
        datas = {}
        title = soup.find('title')
        datas['url']= original_url
        datas['title'] = title.get_text()
        #print self.data
        return datas

    def parse(self, html,original_url):
        if html == None or original_url == None:
            return
        else:
            #self.data['url'] = original_url
            soup = BeautifulSoup(html,'html.parser',from_encoding='utf-8')
            #print soup
            #print soup.find('body').find('a')
            urls = self._geturls(soup,original_url)
            datas = self._getdatas(soup,original_url)
            return urls, datas

