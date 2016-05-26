# -*- coding:utf-8 -*-
import json

import MySQLdb

import date_list


class Date():
    def __init__(self):
        self.datelist = date_list.DataJson()
        self.prueid = []

    def connn_db(self):
        conn = MySQLdb.connect('172.19.2.120', 'root', 'root', 'drug')
        return conn

    # 保存药品名字和id到数据库
    def save_druginfo(self, drugitem):
        conn = MySQLdb.connect('172.19.2.120', 'root', 'root', 'drug')
        cur = conn.cursor()
        cur.executemany('INSERT INTO drug_name (productDrugID, showName) VALUES(%s,%s);', drugitem)
        conn.commit()
        conn.close()
        print u'保存药品名字和id成功'
        self.prueid = []

    # 保存使用说明
    def save_use(self, drugId, productDrugID, Introitem):
        if Introitem is None:
            return
        dp = json.dumps(Introitem,ensure_ascii=False)
        conn = MySQLdb.connect('172.19.2.120', 'root', 'root', 'drug')
        cur = conn.cursor()
        print drugId, productDrugID
        cur.execute('INSERT INTO `instru_use` (drugId,productDrugID,drugUse)VALUES(%s,%s,%s);',
                    (drugId, productDrugID, [dp]))
        conn.commit()
        conn.close()
        print '保存使用说明成功'

    # 保存药品指导
    def save_use_guide(self, drugId, productDrugID, guideitem, ):
        if guideitem is None:
            return
        dp = json.dumps(guideitem,ensure_ascii=False)
        conn = MySQLdb.connect('172.19.2.120', 'root', 'root', 'drug')
        cur = conn.cursor()
        cur.execute('INSERT INTO `drug_guide` (drugId,productDrugID,useGuide) VALUES (%s,%s,%s);',
                    (drugId, productDrugID, [dp]))
        conn.commit()
        conn.close()
        print '保存药品指导成功'

    # 保存所有的的药品信息
    def save_info(self, druginfo):
        if druginfo is None:
            return
        conn = MySQLdb.connect('172.19.2.120', 'root', 'root', 'drug')
        cur = conn.cursor()
        cur.executemany(
            'INSERT INTO drug_info (productDrugID, showName, drugSpec, factory, drugID) VALUES(%s,%s,%s,%s,%s);',
            druginfo)
        conn.commit()
        conn.close()
