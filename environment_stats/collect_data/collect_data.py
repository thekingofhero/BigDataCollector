class collect_data:
    def __init__(self):
        self.baseurl = "http://datacenter.mep.gov.cn/report/air_daily/airDairyCityHour.jsp?city=&startdate=%s%%20%s&enddate=%s%%20%s&page=%s"
        pass
    def collect(self,thread_num = 1,\
                    start_date = '2014-01-01',\
                    start_time = "00:00",\
                    end_date = '2014-01-02',\
                    end_time = '00:00'):
        pass
