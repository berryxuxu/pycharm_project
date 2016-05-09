from urllib import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
be = BeautifulSoup(html)
namelist = be.findAll('span',{'class':'green'})
for name in namelist:
    print name.get_text()