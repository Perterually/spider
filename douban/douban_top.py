# -*- coding:utf-8 -*-
import json
import urllib2

import MySQLdb
from bs4 import BeautifulSoup


class Douban():
    def __init__(self):
        self.url = 'https://movie.douban.com/top250?start='
        self.end = '&filter='
        self.f = open('movie.json', 'w')

    # 获取页面方法
    def getPaper(self, pageIndex):
        url = self.url + str(pageIndex) + self.end
        requsest = urllib2.Request(url)
        reponse = urllib2.urlopen(requsest)
        return reponse.read()

    def getPagerDate(self, pageIndex):
        item = []
        data = self.getPaper(pageIndex)
        soup = BeautifulSoup(data, 'lxml')
        for tag in soup.find_all(id, 'item'):
            try:
                name = tag.find('span', 'title').get_text()
                # <span class="rating_num" property="v:average">9.6</span>
                star = tag.find('span', 'rating_num').get_text()
                # <span class="inq">希望让人自由。</span>
                about = tag.find('span', 'inq').get_text()
                item.append([name, star, about])
            except Exception, ex:
                print Exception, ":", ex
        return item

    # 插入数据库
    def insertDb(self, pageIndex):
        if pageIndex is None:
            return
        item = self.getPagerDate(pageIndex)
        conn = MySQLdb.connect('172.19.2.120', 'root', 'root', 'text')
        cure = conn.cursor()
        cure.executemany('insert into moive (name, star, about) value (%s,%s,%s)', item)
        conn.commit()
        conn.close()

    # 保存到json
    def saveJson(self, item):
        for items in item:
            self.f.write(json.dumps(items))

    # 开始运行函数
    def start(self):
        for paper in range(0, 275, 25):
            data = self.getPagerDate(paper)
            self.saveJson(data)
        self.f.close()


db = Douban()
db.start()
