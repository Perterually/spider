import requests
from pyquery import PyQuery as pq
from lxml import etree
import sqlite3

class Spider:
    def __init__(self):
        self.url = "http://www.ahyycg.cn/NoticeBoard/HC_JiaoYiProGongBu_2014.aspx"
        self.head = {
            'Connection':'keep-alive',
            'Host':'www.ahyycg.cn',
            'Origin':'http://www.ahyycg.cn',
            'Referer':'http://www.ahyycg.cn/NoticeBoard/HC_JiaoYiProGongBu_2014.aspx',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
        }
        self.session = requests.Session()
        self.session.headers.update(self.head)
        self.context = self.session.get(self.url).text
   

    def get_Code(self,html):
        p = etree.HTML(html)
        VIEWSTATE = p.xpath('//*[@id="__VIEWSTATE"]')[0].attrib["value"]
        EVENTVALIDATION = p.xpath('//*[@id="__EVENTVALIDATION"]')[0].attrib['value']
        return  VIEWSTATE,EVENTVALIDATION


    def get_Postdata(self,view,index,code):
        from_date = {
            '__VIEWSTATE':view,
            '__VIEWSTATEGENERATOR':"815A2B7C",
            '__EVENTTARGET':'ctl00$ContentPlaceHolder1$pager1',
            '__EVENTARGUMENT':index,
            '__EVENTVALIDATION':code
        }
        return from_date


    def get_page(self,view,index,code):
        li = []
        s = self.get_Postdata(view,index,code)
        re = self.session.post(self.url,data=s)
        context = re.text
        source = pq(context)

        for data in source('tr'):
            catenname = pq(data).find('td').eq(0).text()
            packname = pq(data).find('td').eq(1).text()
            producpackleve = pq(data).find('td').eq(2).text()
            producpacknum = pq(data).find('td').eq(3).text()
            groupsetid = pq(data).find('td').eq(4).text()
            groupitemid = pq(data).find('td').eq(5).text()
            producompany = pq(data).find('td').eq(6).text()
            bidcomany = pq(data).find('td').eq(7).text()
            groupsetname = pq(data).find('td').eq(8).text()
            groupitemname = pq(data).find('td').eq(9).text()
            speci = pq(data).find('td').eq(10).text()
            li.append([catenname,packname,producpackleve,producpacknum,groupsetid,groupitemid,producompany,bidcomany,groupsetname,groupitemname,speci])
        
        data = li[4:]
        return data
        
    def save_sqlite(self, items):
        conn = sqlite3.connect('drug.db')
        cure = conn.cursor()
        cure.executemany(
            'INSERT INTO info(catenname, packname, producpackleve, producpacknum, groupsetid, groupitemid, producompany,bidcomany, groupsetname, groupitemname,speci) VALUES (?,?,?,?,?,?,?,?,?,?,?)',
            items)
        conn.commit()
        conn.close() 


    def start(self):
        code,view =self.get_Code(self.context)
        for i in range(1,115):
            li = self.get_page(code,i,view)
            self.save_sqlite(li)
            print(i)

s = Spider()
s.start()