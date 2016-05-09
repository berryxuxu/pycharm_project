import urllib2


class Urlopen(object):
    def open(self, newurl):
        if newurl is not None:
            html = urllib2.urlopen(newurl)
            if html.getcode() == 200:
                return html.read()

