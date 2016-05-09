# -*- coding: UTF-8 -*-
import urllib2


class Html_Downloader(object):
    def download(self, new_url):
        html = urllib2.urlopen(new_url)
        if html.getcode() == 200 :
            return html
        else:
            return 'Failed'