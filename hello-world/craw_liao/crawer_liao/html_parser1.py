import urlparse
from bs4 import BeautifulSoup

class Htmlparser(object):

    def parse(self, homeurl, html):
        urls = []
        if html is not None:
            soup = BeautifulSoup(html,'html.parser', from_encoding='utf-8')
            links1 = soup.find('ul',class_= 'uk-nav uk-nav-side',style="margin-right:-15px;" )
            links = links1.findAll('a')
            for link in links:
                url = urlparse.urljoin(homeurl,link['href'])
                urls.append(url)
        #print urls
        return urls


    def last(self,html2):
        dic = {}
        content = []
        soup1 = BeautifulSoup(html2,'html.parser', from_encoding='utf-8')
        aim  = soup1.find('div', class_ = 'x-content', style = 'width:100%')
        title = aim.find('h4').get_text()
        if '/' in title:
            title = title.replace('/', 'or')
        contenttag = aim.findAll('p')
        for i in contenttag:
            content.append(i.get_text())
        dic[title] = content
        return title, dic


