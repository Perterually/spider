# -*- coding:utf-8 -*-
import json
import urllib2

import MySQLdb
from bs4 import BeautifulSoup


class Into:
    def __init__(self):
        self.url = 'http://mobile.gyb365.com/guarder/getDurgInstructions?productID=4c1e09fb-90c5-4925-a28a-970eb2cc4b24'
        self.productID = 'productID='
        self.drugName = '&drugName='
        self.prud = []
        self.pruename = {}
        self.prueinfohtml = ''

    def get_page(self):
        request = urllib2.Request(self.url)
        reponse = urllib2.urlopen(request)
        return reponse.read()

    def get_guide_span(self):
        list = []
        index = 0
        content = self.get_page()
        source = BeautifulSoup(content, 'lxml')
        tag = source.find(id='drugguide')
        for s in tag.find_all('span'):
            list.append(s.string)
        return list

    def get_guide_li(self):
        list = []
        index = 0
        content = self.get_page()
        source = BeautifulSoup(content, 'lxml')
        tag = source.find(id='drugguide')
        for s in tag.find_all('ol'):
            list.append(s.get_text())
        return list

    # 返回名称
    def get_span(self):
        list = []
        index = 0
        content = self.get_page()
        source = BeautifulSoup(content, 'lxml')
        tag = source.find(id='drugmanual')
        try:
            for s in tag.find_all('span'):
                list.append(s.string.encode('utf-8'))
            return list
        except Exception, ex:
            print Exception, ':', ex

    # 返回信息
    def get_p(self):
        list = []
        content = self.get_page()
        source = BeautifulSoup(content, 'lxml')
        tag = source.find(id='drugmanual')
        try:
            for s in tag.find_all('p'):
                list.append(s.get_text().encode('utf-8'))
            return list
        except Exception, ex:
            print Exception, ':', ex

    # 返回说明书的list
    def get_drug_use(self):
        list = []
        span = self.get_span()
        p = self.get_p()
        for row in range(len(span)):
            list.append([span[row] + ':' + p[row]])
        return list

    # 返回指导的list
    def get_drug_guidet(self):
        list = []
        span = self.get_guide_span()
        li = self.get_guide_li()
        for row in range(len(span)):
            list.append([span[row], li[row]])
        return list

    def text(self):
        span = self.get_span()
        p = self.get_p()
        try:
            s = dict(zip(span, p))
            return s
        except Exception, ex:
            print Exception, ':', ex

    def text1(self):
        list = {}

        info = self.get_drug_use()
        map(lambda x: list.setdefault(x.split(':')[0], x.split(':')[1]), info)
        return list

    def insert(self):
        item = self.text()
        df = json.dumps(item, ensure_ascii=False)
        print df
        # conn = MySQLdb.connect(host='172.19.2.120', user='root', passwd='root', db='drug',charset='utf8')
        # cur = conn.cursor()
        # cur.execute('INSERT INTO demo(drugUse)VALUES(%s);',[df])
        # conn.commit()
        # conn.close()
        # print '保存使用说明成功'


info = Into()
info.insert()
