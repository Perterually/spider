import sqlite3
from sqlalchemy import Table, MetaData, Column, Integer, String, create_engine, Text
from sqlalchemy.orm import mapper
import requests,os
from datetime import datetime
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq

class Spider:
    def __init__(self):
        self.url = 'http://218.23.36.222:8020/index.asp'
        self.urls = 'http://218.23.36.222:8020'
        self.head = {
            'Host': '218.23.36.222:8020',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:49.0) Gecko/20100101 Firefox/49.0',
            'Upgrade-Insecure-Requests': '1',
        }

    
    def get_page(self,url):
        re = requests.get(url, headers=self.head)
        content = re.content.decode('gbk')
        return content

    
    def get_link(self,content):
        table = pq(content).find('table').eq(5)
        a = pq(table).find('a').eq(2)
        link = a('a').attr('href')
        url = self.urls + str(link)
        return url
        

    def get_data(self,content):
        li = []
        source = pq(content)
        table = pq(source).find('table').eq(4)
        for date in table('tr'):
            name = pq(date).find('td').eq(0).text()
            name1 = pq(date).find('td').eq(1).text()
            name2 = pq(date).find('td').eq(2).text()
            name3 = pq(date).find('td').eq(3).text()
            name4 = pq(date).find('td').eq(4).text()
            name5 = pq(date).find('td').eq(5).text()
            name6 = pq(date).find('td').eq(6).text()
            name7 = pq(date).find('td').eq(7).text()
            name8 = pq(date).find('td').eq(8).text()
            name9 = pq(date).find('td').eq(9).text()
            name10 = pq(date).find('td').eq(10).text()
            name11 = pq(date).find('td').eq(11).text()
            li.append([name, name1, name2, name3, name4, name5, name6, name7, name8, name9, name10, name11])
        del li[0]
        return li
    
    #创建数据库
    def create_db(self, dataname, tablename):
        #获取当前路径
        root_path =os.getcwd()
        datapth = os.path.join(root_path,dataname)
        
        engine = create_engine('sqlite:///%s' % datapth)

        matedata = MetaData(engine)

        table = Table(tablename,matedata,
            Column('id',Integer,primary_key=True),
            Column('name',Text),
            Column('name1',Text),
            Column('name2',Text),
            Column('name3',Text),
            Column('name4',Text),
            Column('name5',Text),
            Column('name6',Text),
            Column('name7',Text),
            Column('name8',Text),
            Column('name9',Text),
            Column('name10',Text),
            Column('name11',Text),

        )
        matedata.create_all(engine)
        print('创建数据库成功')

    def save_sqlite(self, items):
        conn = sqlite3.connect('drug.db')
        cure = conn.cursor()
        cure.executemany(
            'INSERT INTO info(name, name1, name2, name3, name4, name5, name6, name7, name8, name9, name10, name11) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)',
            items)
        conn.commit()
        conn.close() 
    
    def start(self):
        li = []
        data = self.get_page(self.url)
        
        item = self.get_data(data)
        url = self.get_link(data)
        self.save_sqlite(item)
        li.append(url)
        for i in range(2,183):
            data = self.get_page(li[0])

            item = self.get_data(data)
            print(i,li[0])
            self.save_sqlite(item)
            link = self.get_link(data)
            li.append(link)
            del li[0]
            print(i)




s = Spider()
s.start()
# s.create_db('drug.db','info')