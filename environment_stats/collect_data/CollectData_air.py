import threading
import datetime
from getdata import getdata
import math
class CollectData_Air:
    def __init__(self):
        self.baseurl = "http://datacenter.mep.gov.cn/report/air_daily/airDairyCityHour.jsp?city=&startdate=%s%%20%s&enddate=%s%%20%s&page=1"
        pass

    def get_task_days(self,start_date,start_time,end_date,end_time):
        task_days = []
        start_t = datetime.datetime.strptime("%s %s"%(start_date,start_time),\
                                            "%Y-%m-%d %H:%M")
        end_t = datetime.datetime.strptime("%s %s"%(end_date,end_time),\
                                            "%Y-%m-%d %H:%M")
        days = (end_t - start_t).days
        #total tasks,hours left
        for i in range(1,days+2):
            s = str(start_t + datetime.timedelta(i-1)).split(" ")
            e = str(start_t + datetime.timedelta(i)).split(" ")
            if (start_t + datetime.timedelta(i)) > end_t:
                e = str(end_t).split(" ")
            task_days.append((s,e))
        return task_days

    def collect(self,thread_num = 1,\
                    start_date = '2014-01-01',\
                    start_time = "00:00",\
                    end_date = '2014-01-01',\
                    end_time = '01:00'):
        total_tasks = self.get_task_days(start_date,start_time,end_date,end_time)
        url_list = []
        for s,e in total_tasks:
            url = self.baseurl%(s[0],s[1],e[0],e[1])
            url_list.append(url)
        max_task_num_per_thread = int(math.ceil(len(url_list)/float(thread_num)))
        temp = [url_list[i:i+max_task_num_per_thread] for i in range(0,len(url_list),max_task_num_per_thread)]
        thread_list = []
        for temp_i in temp:
            print(temp_i)
            t = threading.Thread(target=getdata,args=[temp_i])
            thread_list.append(t)
            t.start()
        for t in thread_list:
            if t.is_alive():
                t.join()

if __name__ == '__main__':
    obj = CollectData_air()
    obj.collect(thread_num = 10,\
                start_date = '2014-01-01',\
                start_time = '00:00',\
                end_date = "2016-01-01",\
                end_time = "00:00")
