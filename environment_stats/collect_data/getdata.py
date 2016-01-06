try:
    from urllib.request import urlopen,Request
except ImportError:
    from urllib2 import urlopen,Request
from bs4 import BeautifulSoup
    
temp = ''
#url = urlopen('http://datacenter.mep.gov.cn/report/air_daily/air_dairy.jsp?city=&startdate=2012-12-05&enddate=2015-12-22&page=1')
url = urlopen('http://datacenter.mep.gov.cn/report/air_daily/airDairyCityHour.jsp?city=&startdate=2014-01-01%2008:00&enddate=2014-01-01%2011:00&page=2')
#with open('./a.xml') as url:
if 1:
    temp = url.read()
    temp = temp.replace("\n",'')
    soup = BeautifulSoup(temp,"lxml")
    for tr in soup.find_all("tr"):
    	if len(tr.attrs) == 2:
            keys = tr.attrs.keys()
            keys.sort()
            if cmp(keys,['height', 'style']) == 0:
                #other info
                if tr['height'] == "25":
                    pass
                #data
                elif tr['height'] == "30":
                    row = ''
                    for child in tr:
                        if child.string is None:
                            continue
                        if row == '':
                            row = ''.join([row,child.string])
                        else:
                            row = ''.join([row,',',child.string])
                    print(row.strip(' ').strip(","))
#                        for c in child.next_siblings:
#                            try:
#                                print(c.string)
#                            except:
#                                import sys
#                                reload(sys)
#                                sys.setdefaultencoding('utf8')
#                                print(c.string)
    #print (len(soup.find('tr')))
