import requests
import time
from save_excel import Excel
from save_sqlite import SaveSQl

class Spider():
    def __init__(self):
        self.url = 'http://101.201.155.40:8002/BaList.aspx'
        self.urls = 'http://101.201.155.40:8002/BaInfo.ashx'
        self.head = {
                'Connection':'keep-alive',
                'Host':'101.201.155.40:8002',
                'Upgrade-Insecure-Requests':'1',
                'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'
                }
        
        self.session = requests.Session()
        self.session.headers.update(self.head)
        self.session.get(self.url) 
        self.sqlite = SaveSQl('drug.db')
        self.excel = Excel('drug.db')

    def form_data(self,page):
        nd = int(time.time()*1000)

        data = {
            '_search':'false',
            'nd':nd,
            'rows':15,
            'page':page,
            'sidx':'GPARTID',
            'sord':'asc'
        }
        return data
    
    def get_data(self,page):
        li = []
        data = self.form_data(page)
        rq = self.session.post(self.urls,data=data)
        date = rq.json()
        rows = date['rows']
        for i in rows:
            li.append(i['cell'])
        return li

    
    def start(self):
        for i in range(276):
            item = self.get_data(i)
            print(i)
            self.sqlite.insert(item)
            print(i)
        row = self.excel.get_count()
        self.excel.save_excel(row,'2016.xls')
s = Spider()
s.start()