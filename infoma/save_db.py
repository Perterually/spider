# -*- coding:utf-8 -*-
import MySQLdb

class SaveDb:
    def save_db_id_name(self,item):
        if item is None:
            return
        conn = MySQLdb.connect('172.19.2.120', 'root', 'root', 'drug')
        cur = conn.cursor()
        print len(item)
        cur.executemany('INSERT INTO drug_info (productDrugID, showName, drugSpec, factory) VALUES(%s,%s,%s,%s);', item)