# -*- coding:utf-8 -*-
import json

import MySQLdb


class ReadData():
    def __init__(self):
        self.list = []

    def get_count(self):
        conn = MySQLdb.connect('172.19.2.120', 'root', 'root', 'drug')
        cur = conn.cursor()
        cur.execute("select count(*) from instru_use")
        data = cur.fetchall()
        # 从tuple中提取数据
        before = data[0]
        ofter = before[0]
        conn.commit()
        conn.close()
        return ofter

    def get_date_len(self, id):
        conn = MySQLdb.connect('172.19.2.120', 'root', 'root', 'drug')
        cur = conn.cursor()
        cur.execute("select drugUse from instru_use where id = %d" % id)
        data = cur.fetchall()
        # 从tuple中提取数据
        before = data[0]
        after = before[0]
        date = json.loads(after, encoding='utf8')
        conn.commit()
        conn.close()
        return len(date)

    def get_date(self, id):
        conn = MySQLdb.connect('172.19.2.120', 'root', 'root', 'drug')
        cur = conn.cursor()
        cur.execute("select drugUse from instru_use where id = %d" % id)
        data = cur.fetchall()
        # 从tuple中提取数据
        before = data[0]
        after = before[0]
        date = json.loads(after, encoding='utf8')
        conn.commit()
        conn.close()
        return date
