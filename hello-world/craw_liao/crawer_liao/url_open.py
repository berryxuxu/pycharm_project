#coding:utf-8
import urllib2
class Urlopen(object):
    def open(self, newurl):
        if newurl is not None:
            # cookie = cookielib.CookieJar() #创建cookiejar对象来保存cookie
            # handler = urllib2.HTTPCookieProcessor(cookie)  #创建COOKIE处理器
            # opener = urllib2.build_opener(handler) #通过handler来创建opener
            # values = {'redirect':", 'rememberme':", 'submit':'OK, Let Me In!'}
            # datas = urllib.urlencode(values)
            #urllib2.install_opener(opener)
            headers1 = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0) '}
            req = urllib2.Request(newurl, headers = headers1)
            content = urllib2.urlopen(req)
            if content.getcode() == 200:
                return content


