#coding:utf-8
class Urlmanager(object):


    def getone(self, urls):
        if urls is not None:
            a = urls[0]
            urls.remove(urls[0])
            return a

    def notfinished(self, urls):
        if len(urls) != 0:
            return True
        else:
            return False


