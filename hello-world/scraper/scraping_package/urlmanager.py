# -*- coding: UTF-8 -*-
class UrlManager(object):
    def __init__(self):
        self.oldurl = set()
        self.newurl = set()

    def add_new_url(self, entranceURL):
        if entranceURL == None:
            return
        if entranceURL not in self.oldurl and entranceURL not in self.newurl:
            self.newurl.add(entranceURL)
            return
        else:
            return

    def has_new_urls(self):
        if len(self.newurl) !=  0:
            return True
        else:
            return False

    def get_new_url(self):
        aurl = self.newurl.pop()
        self.oldurl.add(aurl)
        return aurl

    def add_new_urls(self, new_urls):
        for url in new_urls:
            self.add_new_url(url)
        return