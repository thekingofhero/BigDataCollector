try:
    from urllib.request import urlopen,Request
except ImportError:
    from urllib2 import urlopen,Request
from bs4 import BeautifulSoup

temp = ''
url = urlopen('http://datacenter.mep.gov.cn/report/air_daily/air_dairy.jsp?city=&startdate=2012-12-05&enddate=2015-12-22&page=1')
temp = url.read().decode('utf8')
soup = BeautifulSoup(temp)
print (soup.find('tr'))
