#coding:utf-8
from urllib import urlretrieve
import urllib2

class Output(object):
    def output(self, count, image):
        #print image
        f = open('D://PIC/'+str(count)+'.jpg','wb')
        f.write(image.read())
        f.close()
        #jpg = urlretrieve(image,'D://PIC/'+str(count)+'.html')


