#from multiprocessing import Process,Manager
from threading import Thread,Lock
from GetInfo.GetStockPriceInfo_job import GetStockpriceInfo_job
from config import local_config
def GetStockPriceInfo(market,Stock_List,queue):
    step_size = local_config()['step_size']
    partitions = [Stock_List[i:i+step_size] for i in range( 0,\
                                                                  len(Stock_List),\
                                                                  step_size)]
    proc_list = []
    lock = Lock()
    for part in partitions:
        all_url = ''.join([str_i + ',' for str_i in part])
        each_job = GetStockpriceInfo_job(market,all_url)
        proc = Thread(target = each_job.GetPriceInfo,args=[queue,lock])
        proc.start()
        proc_list.append(proc)
    
    for proc in proc_list:
        if proc.is_alive():
            proc.join()

