import urlparse
from bs4 import BeautifulSoup

class Htmlparser(object):
    # def __init__(self):
    #     self.n = ''
    def parse(self, enterurl, html):
        urls = set()
        if html is not None:
            soup = BeautifulSoup(html,'html.parser', from_encoding='utf-8')
            links = soup.find_all('a',class_='preview')

            for link in links:
                url = urlparse.urljoin(enterurl,link['href'])
                urls.add(url)
        #print urls
        return urls

    def getone(self, urls):

        if urls is not None:
            return urls.pop()


    def hasimage(self,urls):
        if len(urls) != 0:
            return True
        else:
            return False

    def last(self,enterurl, html2):
        #print urls.pop()
        soup1 = BeautifulSoup(html2,'html.parser', from_encoding='utf-8')
        #print soup1
        link = soup1.find('img',id = 'wallpaper')
        image = urlparse.urljoin(enterurl,link['src'])
        return image


