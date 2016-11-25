# -*- coding:utf-8 -*-
import sqlite3
from urllib.parse import urlencode
import sys
import pymysql
import requests
from pyquery import PyQuery as pq


class Info:
    def __init__(self):
        self.header = {
            'Host': '116.252.221.174',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'
        }
        self.session = requests.Session()
        self.session.headers.update(self.header)
        self.url = 'http://116.252.221.174/guawang_sys/index_gw.asp?guawangid=FCK11122420140610t '
        self.urls = 'http://116.252.221.174/guawang_sys/guawang_tables.asp?guawangid=FCK11122420140610t '
        self.urlss = 'http://116.252.221.174/guawang_sys/guawang_tables.asp?'
        self.li = []

    def get_url(self, index):
        param = {
            'page': index,
            'search_1': '',
            'search_2': '',
            'search_3': '',
            'search_4': '',
            'pq': '',
            'guawangid': 'FCK11122420140610t '
        }
        return self.urlss + urlencode(param)

    def get_data(self, index):
        li = []
        self.session.get(self.url)
        rs = self.session.get(self.get_url(index))
        print(self.get_url(index))
        content = rs.content.decode('gbk')
        try:
            source = pq(content)
            for data in source('table'):
                catenname = pq(data).find('td').eq(0).text()
                packname = pq(data).find('td').eq(1).text()
                producpackleve = pq(data).find('td').eq(2).text()
                producpacknum = pq(data).find('td').eq(3).text()
                groupsetid = pq(data).find('td').eq(4).text()
                groupitemid = pq(data).find('td').eq(5).text()
                producompany = pq(data).find('td').eq(6).text()
                bidcomany = pq(data).find('td').eq(7).text()
                groupsetname = pq(data).find('td').eq(8).text()
                groupitemname = pq(data).find('td').eq(9).text()
                speci = pq(data).find('td').eq(10).text()
                model = pq(data).find('td').eq(11).text()
                # perforcompo = pq(data).find('td').eq(12).text()
                # packspeci = pq(data).find('td').eq(13).text()
                # packmatel = pq(data).find('td').eq(14).text()
                # brand = pq(data).find('td').eq(15).text()
                # unit = pq(data).find('td').eq(16).text()
                # winbidprice = pq(data).find('td').eq(17).text()
                # cate = pq(data).find('td').eq(18).text()
                # a = pq(data).find('td').eq(19).text()
                li.append([
                    catenname, packname, producpackleve, producpacknum, groupsetid, groupitemid, producompany,
                    bidcomany, groupsetname, groupitemname, speci, model,])
            return li
        except Exception:
            print(Exception)

    def listprocess(self, data, ):
        if data is None:
            return None
        del data[0:4]
        try:
            data.pop()
            return data
        except Exception:
            print(Exception)

    def create_db(self):
        conn = sqlite3.connect('drug.db')
        sql = 'CREATE TABLE info (id integer PRIMARY KEY AUTOINCREMENT NOT NULL,catenname text(128),packname text(128),producpackleve text(128),producpacknum text(128),groupsetid text(128),groupitemid text(128),producompany text(128),bidcomany text(128),groupsetname text(128),groupitemname text(128),speci text(128),model text(128),perforcompo text(128),packspeci text(128),packmatel text(128),brand text(128),unit text(128),winbidprice text(128),cate text(128),a text(128));'
        conn.execute(sql)

    def save_sql(self, items):
        conn = pymysql.connect('172.19.2.120', 'root', 'root', 'drug')
        cure = conn.cursor()
        cure.executemany(
            'INSERT INTO info(catenname, packname, producpackleve, producpacknum, groupsetid, groupitemid, producompany,bidcomany, groupsetname, groupitemname, speci, model, perforcompo,packspeci,packmatel,brand,unit,winbidprice) VALUE (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            items)
        conn.commit()
        conn.close()

    def save_sqlite(self, items):
        conn = sqlite3.connect('drug.db')
        cure = conn.cursor()
        cure.executemany(
            'INSERT INTO info(catenname, packname, producpackleve, producpacknum, groupsetid, groupitemid, producompany,bidcomany, groupsetname, groupitemname, speci, model) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)',
            items)
        conn.commit()
        conn.close()

    def Start(self):
        for i in range(1, 100):
            data = self.get_data(i)
            detail = self.listprocess(data)
            if detail == None:
                # self.li.append(i)
            # self.save_sqlite(detail)
                print(detail)
            print(i)             


i = Info()
i.create_db()
