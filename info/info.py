import sqlite3
from urllib.parse import urlencode

import requests
from pyquery import PyQuery as pq


class Drug:
    def __init__(self):
        self.url = "http://www.drugnet.com.cn/BidPurchasing/BidReagent?id=22964"
        self.urls = "http://www.drugnet.com.cn/BidPurchasing/BidReagent/22964"
        self.session = requests.Session()

    def get_url(self, index):
        param = {
            'PageIndex': index
        }
        return self.urls + '?' + urlencode(param)

    def get_date(self, index):
        li = []
        self.session.get(self.url)
        rs = self.session.get(self.get_url(index))
        content = rs.content.decode('utf-8')
        source = pq(content)
        for data in source('tr'):
            catenname = pq(data).find('td').eq(0).text()
            packname = pq(data).find('td').eq(1).text()
            producpackleve = pq(data).find('td').eq(2).text()
            producpacknum = pq(data).find('td').eq(3).text()
            groupsetid = pq(data).find('td').eq(4).text()
            groupitemid = pq(data).find('td').eq(5).text()
            producompany = pq(data).find('td').eq(6).text()
            bidcomany = pq(data).find('td').eq(7).text()
            li.append(
                [catenname, packname, producpackleve, producpacknum, groupsetid, groupitemid, producompany, bidcomany])
        del li[0]
        print(li[0][2])

    def save_db(self, item):
        conn = sqlite3.connect('drug.db')
        cure = conn.cursor()
        cure.executemany(
            'INSERT INTO info(catenname, packname, producpackleve, producpacknum, groupsetid, groupitemid, producompany,bidcomany) VALUES (?,?,?,?,?,?,?,?)',item)
        conn.commit()
        conn.close()


    def start(self):
        for i in range(339,387):
            item = self.get_date(i)
            self.save_db(item)
            print(i)

d = Drug()
d.get_date(1)
