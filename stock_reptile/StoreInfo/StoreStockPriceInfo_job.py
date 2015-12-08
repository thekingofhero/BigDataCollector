from config import local_config
import time
class StoreStockPriceInfo_job:
    def __init__(self,market):
        self.market = market
    
    def StorePriceInfo(self,queue,lock,output_media):
        output_type = local_config()['output_type']
        while True:
            lock.acquire()
            if output_type == 'csv':
                while not queue.empty():
                    temp = queue.get() + str(queue.qsize()) +'\n'
                    output_media.write(temp)
            time.sleep(2)
            lock.release()
