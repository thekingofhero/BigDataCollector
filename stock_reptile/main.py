#-*- coding:utf-8 -*-
import urllib
from urllib import request
import time
import os
from multiprocessing import Process,Manager
from GetInfo.GetStockPriceInfo import GetStockPriceInfo
from StoreInfo.StoreStockPriceInfo import StoreStockPriceInfo

def GetStockList():
    Stock_Dic = {}
    if os.path.isfile("stock_list_shA.csv"):
        Stock_Dic['sh'] = []
        with open('stock_list_shA.csv',mode = 'r',encoding='utf-8') as fp_shA:
            for line in fp_shA:
                try:
                    Stock_Dic['sh'].append('sh' + str(int(line.split(',')[0])))  
                except:
                    print(line.split(',')[0])
    return Stock_Dic

def main():
    Stock_Dic = GetStockList()
    for market in Stock_Dic.keys():
        manager = Manager()
        message_queue = manager.Queue()
        proc_Producer = Process(target = GetStockPriceInfo,args = [market,Stock_Dic[market],message_queue])
        proc_Consumer = Process(target = StoreStockPriceInfo,args = [market,Stock_Dic[market],message_queue])
        proc_Producer.start()
        proc_Consumer.start()
        proc_Producer.join()
        proc_Consumer.join()
            
if __name__ == '__main__':
    main()
