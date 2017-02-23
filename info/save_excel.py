# -*- coding:utf-8 -*-
"""
python 3
"""
from openpyxl import Workbook
import sqlite3

class Excel():
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.conn = sqlite3.connect('drug.db')
        self.cur = self.conn.cursor()
        self.li = []

    #get data
    def get_date(self, id):
        self.cur.execute("SELECT * FROM info WHERE id=%d" % id)
        data = self.cur.fetchall()
        t = data[0]
        li = list(t)
        return li

    #get total row
    def get_row(self):
        self.cur.execute("SELECT COUNT(*) from info")
        data = self.cur.fetchall()
        li = data[0]
        row = li[0]
        return row
        
    def start(self):
        row = self.get_row()
        for i in range(1,row+1):
            data = self.get_date(i)
            print(i)
            self.ws.append(data)
        self.conn.commit()
        self.conn.close()
        self.wb.save('江苏省.xlsx')
        print("Done")
       
    
s = Excel()
s.start()
