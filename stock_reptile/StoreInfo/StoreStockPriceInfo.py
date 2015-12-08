#from multiprocessing import Process,Manager
from threading import Thread,Lock
from config import local_config
from StoreInfo.StoreStockPriceInfo_job import StoreStockPriceInfo_job
import os

def StoreStockPriceInfo(market,Stock_List,queue):
    with open(os.path.join(local_config()['install_path'],'output.csv'),'w',encoding='utf-8') as fp_w:
        consumer_num = local_config()['consumer_num']
        lock = Lock()
        consumer_proc_list = []
        for i in range(consumer_num):
            each_job = StoreStockPriceInfo_job(market)
            consumer_proc = Thread(target =each_job.StorePriceInfo ,args=[queue,lock,fp_w])
            consumer_proc.start()
            consumer_proc_list.append(consumer_proc)
        for proc in consumer_proc_list:
            if proc.is_alive():
                proc.join()