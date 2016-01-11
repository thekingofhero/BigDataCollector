#-*- coding:utf-8 -*-
try:
    from urllib.request import urlopen,Request
except ImportError:
    from urllib2 import urlopen,Request
from bs4 import BeautifulSoup
import re
import time
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
def get_pages(soup,url):
    #page number
    page_rela = []
    for b in soup.find_all("b"):
        for child in b:
            if b.string is None:
                continue
            page_rela.append(int(b.string))
    total_rec,total_page,each_page = page_rela
    pages = [''.join([url[:-1],str(i)]) for i in range(1,total_page+1)]
    return pages

def get_envdata(soup,file_p,head_flag):
    #env data
    for tr in soup.find_all("tr"):
        if len(tr.attrs) == 2:
            keys = tr.attrs.keys()
            keys.sort()
            if cmp(keys,['height', 'style']) == 0:
                #other info
                if tr['height'] == "25":
                    for child in tr:
                        if child.string is None:
                            continue
                    pass
                #data
                elif tr['height'] == "30":
                    row = ''
                    #delete "全 国 城 市 空 气 质 量 小 时 报"
                    if len(tr) < 13:
                        continue
                    for child in tr:
                        if child.string is None:
                            child.string = 'None'
                           # continue
                        if child.string == ' ':
                            continue
                        if row == '':
                            row = ''.join([row,child.string])
                        else:
                            row = ''.join([row,',',child.string])
                    #head needs only once
                    if '序号' in row \
                        and head_flag is False:
                        continue
                    print >> file_p ,row.strip(' ').strip(",")
        #print (len(soup.find('tr')))

def getdata(url_list):    
    temp = ''
    #url = urlopen('http://datacenter.mep.gov.cn/report/air_daily/air_dairy.jsp?city=&startdate=2012-12-05&enddate=2015-12-22&page=1')
    #    url = urlopen('http://datacenter.mep.gov.cn/report/air_daily/airDairyCityHour.jsp?city=&startdate=2014-01-01%2008:00&enddate=2014-01-01%2011:00&page=2')
    for url_per in url_list:
        url = urlopen(url_per)
        temp = url.read()
        temp = temp.replace("\n",'')
        soup = BeautifulSoup(temp,"lxml")
#        with open(r'./data_xml/%s.xml'%(url_per.split(".jsp?")[1]),'w') as fpw:
#            fpw.write(soup.prettify())
        #get all pages
        with open(r'./data_csv/%s.csv'%(url_per.split(".jsp?")[1][0:-7]),'w') as fpw:
            pages = get_pages(soup,url_per)
            for i,page in enumerate(pages):
                soup = BeautifulSoup(urlopen(page).read().replace("\n",""))
                get_envdata(soup,fpw,True if i == 0 else False)
                time.sleep(5)

