# -*- coding:utf-8 -*-
import json
import urllib2

import MySQLdb


class PrueInfo:
    def __init__(self):
        self.prueinfo = []
        self.content = 'application/json;charset=UTF-8'
        self.headers = {'Content-Type': self.content}
        self.url = 'http://mobile.gyb365.com/guarder/Controller/MicroMessage/drugSearchMore'

    def get_paper(self, prueid):
        postdate = '{"productDrugID":"%s"}' % prueid
        request = urllib2.Request(self.url, postdate, headers=self.headers)
        data = urllib2.urlopen(request)
        data_json = data.read()
        read_json = json.loads(data_json)
        return read_json

    def get_into(self, jsondata):
        data = jsondata['data']
        try:
            drugData = data['drugData']
            drugList = drugData['drugList']
            for prueinto in drugList:
                self.prueinfo.append(
                    [prueinto['productDrugID'], prueinto['showName'], prueinto['drugSpec'], prueinto['factory']])
        except Exception, ex:
            print Exception, ':', ex
        return self.prueinfo

    def inser_db(self, prueid):
        jsondata = self.get_paper(prueid)
        item = self.get_into(jsondata)
        print item
        conn = MySQLdb.connect('172.19.2.120', 'root', 'root', 'drug')
        cur = conn.cursor()
        cur.executemany('INSERT INTO drug_info (productDrugID, showName, drugSpec, factory) VALUES(%s,%s,%s,%s);', item)
        conn.commit()
        conn.close()

    def get_prueinfoinserdb(self, prueitem):
        for item in prueitem:
            self.inser_db(item)
            self.prueinfo = []
