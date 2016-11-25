# -*- coding:utf-8 -*-
import sqlite3
from urllib.parse import urlencode

import requests
from pyquery import PyQuery as pq


class lanzhou():
    def __init__(self):
        self.head = {
            'Host': 'www.wz-yy.net',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'
        }
        self.url = 'http://www.wz-yy.net/lzzqyccg/jggs.asp'

    def get_url(self, index):
        param = {
            'page': index,
            'ypname': ''
        }
        return self.url + urlencode(param)

    def add_cookie(self, cookie):
        head = {
            'Cookie': cookie,
            'Host': 'www.wz-yy.net',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'
        }
        return head

    def get_cookie(self, cookie):
        for i in cookie:
            s = i[0]
            a = i[1]
            return s + '=' + a

    def get_date(self, index):
        li = []
        rs = requests.get('http://www.wz-yy.net/lzzqyccg/jggs.asp?page=%d&ypname=' % index)
        data = rs.content.decode('gbk')
        try:
            content = pq(data)
            for tr in content('tr'):
                catenname = pq(tr).find('td').eq(0).text()
                packname = pq(tr).find('td').eq(1).text()
                producpackleve = pq(tr).find('td').eq(2).text()
                producpacknum = pq(tr).find('td').eq(3).text()
                groupsetid = pq(tr).find('td').eq(4).text()
                groupitemid = pq(tr).find('td').eq(5).text()
                producompany = pq(tr).find('td').eq(6).text()
                bidcomany = pq(tr).find('td').eq(7).text()
                groupsetname = pq(tr).find('td').eq(8).text()
                groupitemname = pq(tr).find('td').eq(9).text()
                speci = pq(tr).find('td').eq(10).text()
                model = pq(tr).find('td').eq(11).text()
                perforcompo = pq(tr).find('td').eq(12).text()
                packspeci = pq(tr).find('td').eq(13).text()

                li.append([
                    catenname, packname, producpackleve, producpacknum, groupsetid, groupitemid, producompany,
                    bidcomany, groupsetname, groupitemname, speci, model, perforcompo, packspeci])
            return li
        except Exception:
            print(Exception)

    def listprocess(self, data):
        if data is None:
            return None
        try:
            data.pop()
            return data
        except Exception:
            print(Exception)

    def create_db(self):
        sql = 'CREATE TABLE info (id integer PRIMARY KEY AUTOINCREMENT NOT NULL,catenname text(128),packname text(128),producpackleve text(128),producpacknum text(128),groupsetid text(128),groupitemid text(128),producompany text(128),bidcomany text(128),groupsetname text(128),groupitemname text(128),speci text(128),model text(128),perforcompo text(128),packspeci text(128));'

    def save_sql(self, items):
        conn = sqlite3.connect('info.db')
        cure = conn.cursor()
        cure.executemany(
            'INSERT INTO info(catenname, packname, producpackleve, producpacknum, groupsetid, groupitemid, producompany,bidcomany, groupsetname, groupitemname, speci, model, perforcompo,packspeci) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
            items)
        conn.commit()
        conn.close()

    def start(self):
        for i in range(1, 1084):
            data = self.get_date(i)
            li = self.listprocess(data)
            self.save_sql(li)
            print(i)


lz = lanzhou()
lz.start()
