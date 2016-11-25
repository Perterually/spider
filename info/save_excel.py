# -*- coding:utf-8 -*-
"""
python 2.7
"""
from openpyxl import Workbook
import sqlite3

class Excel():
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.li = []

    def get_date(self, id):
        conn = sqlite3.connect('drug.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM info WHERE id=%d" % id)
        data = cur.fetchall()
        t = data[0]
        li = list(t)
        return li
        conn.commit()
        conn.close()

    def start(self):
        for i in range(1,2621):
            data = self.get_date(i)
            print(i)
            self.ws.append(data)
        self.wb.save('info.xlsx')

s = Excel()
s.start()
