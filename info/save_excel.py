# -*- coding:utf-8 -*-
"""
python 3
"""
from openpyxl import Workbook
import sqlite3

class Excel():
    """initia workbook sqlite3 connect.

    :param name: Database name
    """

    def __init__(self,name):
        """ini
        :
        """
        self.wb = Workbook()
        self.ws = self.wb.active
        self.conn = sqlite3.connect(name)
        self.cur = self.conn.cursor()

        self.li = []

    def get_date(self, number):
        """Get a line data.

        :param number: id
        """
        self.cur.execute("SELECT * FROM info WHERE id=%d" % number)
        data = self.cur.fetchall()
        t = data[0]
        li = list(t)
        return li
        self.conn.commit()
        self.conn.close()

    def get_count(self):
        """Get row total

        """
        self.cur.execute("select count(*) from info")
        data = self.cur.fetchall()
        row = data[0]
        return row[0]
        
    
    def save_excel(self,row,name):
        """Save Excel.

        :param row: All row
        :param name: Excel file name
        """
        for i in range(1,row+1):
            data = self.get_date(i)
            print("Save %d" % i)
            self.ws.append(data)
        self.wb.save(name)
    
