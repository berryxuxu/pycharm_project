class Urlman(object):
    def __init__(self):
        self.crawed = set()
        self.not_crawed = set()


    def addurl(self, url):
        if url == None:
            return
        if url not in self.crawed and url not in self.not_crawed:
            self.not_crawed.add(url)

    def addurls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.addurl(url)


    def has_url(self):
        if len(self.not_crawed) != 0:
            return True
        else:
            return False

    def getone(self):
        if len(self.not_crawed) != 0:
            url = self.not_crawed.pop()
            self.crawed.add(url)
            return url






