#-*- coding: utf-8 -*-
from pyquery import PyQuery as pq
import MySQLdb
import xlsxwriter
import csv

class stock:

    def __init__(self):
        self.url = 'http://yunvs.com/list/mai_'
        self.end = '.html'
        self.file = file('stock.csv','wb')
        self.write = csv.writer(self.file)
        self.write.writerow(['代码','股票','相关概念'])
    #获页面数据存入list
    def getDate(self,pageIndex):
        list = []
        source = pq(self.url + str(pageIndex) + self.end)
        for data in source('tr'):
            code = pq(data).find('td').eq(0).text()
            name = pq(data).find('td').eq(1).text()
            len_int = pq(data).find('td').eq(5)
            for i in range(len(pq(len_int).find('a'))):
                about = pq(len_int).find('a').eq(i).text()
                list.append([code,name,about])
        return list

    #保存到mysql
    def insertDb(self,pageIndex):
        item = self.getDate(pageIndex)
        conn = MySQLdb.connect('172.19.2.120','root','root','text')
        cure = conn.cursor()
        cure.executemany('insert into stock (code,name,about) value (%s,%s,%s)',item)
        conn.commit()
        conn.close()

    #定义选择保存的方法
    def select(self,endPage):
        num = 1
        for i in xrange(num,endPage):
            #调用保存到数据库方法
            self.insertDb(i)
            print u'正在保存第%d页到数据库' % i
    print u'已经保存到数据库'

ss = stock()
ss.select(2)