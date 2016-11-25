import sqlite3

import pymysql
import requests


class demo():
    def __init__(self):
        self.url = 'http://101.201.155.40:8002/BidIfo.ashx'
        self.head = {
            'Host': '101.201.155.40:8002',
            'Origin': 'http://101.201.155.40:8002',
            'Referer': 'http://101.201.155.40:8002/BidList.aspx',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        self.session = requests.Session()
        self.session.headers.update(self.head)

    def post_date(self, index):
        postdata = {
            '_search': 'false',
            'nd': '1470210512509',
            'rows': '15',
            'page': index,
            'sidx': 'GPARTID',
            'sord': 'asc'
        }
        return postdata

    def create_db(self):
        conn = sqlite3.connect('xiaogan.db')
        sql = 'CREATE TABLE info (id integer PRIMARY KEY AUTOINCREMENT NOT NULL,catenname text(128),packname text(128),producpackleve text(128),producpacknum text(128),groupsetid text(128),groupitemid text(128),producompany text(128),bidcomany text(128),groupsetname text(128),groupitemname text(128),speci text(128),model text(128));'
        conn.execute(sql)

    def get_date(self, index):
        li = []
        data = self.post_date(index)
        rs = self.session.post(self.url, data=data)
        s = rs.json()
        cell = s['rows']
        for i in cell:
            data = i['cell']
            li.append(data)
        return li

    def save_sqlite(self, items):
        conn = sqlite3.connect('xiaogan.db')
        cure = conn.cursor()
        cure.executemany(
            'INSERT INTO info(catenname, packname, producpackleve, producpacknum, groupsetid, groupitemid, producompany,bidcomany, groupsetname, groupitemname, speci, model) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)',
            items)
        conn.commit()
        conn.close()

    def save_mysql(self, items):
        conn = pymysql.connect('127.0.0.1', 'root', 'root', 'drug', 32769, charset='utf8mb4',)
        cur = conn.cursor()
        sql = 'INSERT INTO info(catenname, packname, producpackleve, producpacknum, groupsetid, groupitemid, producompany,bidcomany, groupsetname, groupitemname, speci, model) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cur.executemany(sql, items)
        conn.commit()
        conn.close()

    def start(self):
        for i in range(1, 1608):
            item = self.get_date(i)
            self.save_mysql(item)
            print(i)

s = demo()
s.start()
