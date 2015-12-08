from urllib import request
import time
class GetStockpriceInfo_job:
    def __init__(self,market,stocks_url):
        self.market = market
        self.all_stocks = stocks_url
    def GetPriceInfo(self,queue,lock):
        while True:
            with request.urlopen(''.join(["http://hq.sinajs.cn/list" ,'=',self.all_stocks])) as url:
                 deco = url.read().decode('gbk').split('\n')
                 lock.acquire()
                 #print(deco)
                 for deco_i in deco:
                     if deco_i != '' :
                         queue.put(deco_i) 
                 lock.release()
            time.sleep(1)
