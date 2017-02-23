import requests
import re
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
import time
import sqlite3

class Hospital:
    
    def __init__(self):
        self.url = "http://yyk.99.com.cn"
        self.url_city = "http://yyk.99.com.cn/city.html"
        self.head = {
            "Connection":"keep-alive",
            "Host":"yyk.99.com.cn",
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",      
        }
        self.li = []
        

    #get html data
    def get_html(self,url):
        rp = self.session.get(url)
        return rp.text

    #get city site url
    def getCityUrl(self,url):
        li = []
        souce = requests.get(url,headers=self.head).text
        bs = BeautifulSoup(souce,'lxml')
        for tag in bs.find_all(class_='cityarea'):
            for link in tag.find_all('a'):
                city = link.get('href')
                city_url = self.url + city
                li.append(city_url)
        return li

    #get hospotal site url
    def getHosUrl(self,url):
        li = []
        souce = requests.get(url,headers=self.head).text
        bs = BeautifulSoup(souce,'lxml')
        for tag in bs.find_all(class_="tablist"):
            for lis in tag.find_all('li'):
                for link in lis.find_all("a"):
                    site = link.get("href")
                    li.append(site)
        return li
    

    def getHosDate(self,url):
        li = []
        li2 = []
        li3 = []
        li4 = []
        content = requests.get(url,headers=self.head).text
        bs = BeautifulSoup(content,'lxml')
        for tag in bs.find_all(class_="bread_nav clearbox"):
            for a in tag.find_all("a"):
                data = a.string
                li.append(data)

        for tag in bs.find_all(class_="hospital_name clearbox"):
            for h in tag.find_all("h1"):
                data = h.string.strip()
                li.append(data)
        
        for tag in bs.find_all(class_="hpi_content clearbox"):
            for litag in tag.find_all("li"):
                li2.append(litag.text.strip())
                for span in litag.find_all("span"):
                    li3.append(span.string)

        try:    
            #city
            city = li[2]
            #area
            area = li[3]
            #name
            name = li[4]
            #last date
            del li3[3]
            li3.insert(0,city)
            li3.insert(1,area)
            li3.insert(2,name)
            if len(li3) == 7:
                li4.append(li3)
            else:
                self.li.append(url)
        except Exception:
            print(Exception)
        
        return li4
    
    def create_db(self):
        conn = sqlite3.connect('drug.db')
        sql1 = 'DROP TABLE IF EXISTS `info`;'
        conn.execute(sql1)
        sql = 'CREATE TABLE info (id integer PRIMARY KEY AUTOINCREMENT NOT NULL,catenname text(128),packname text(128),producpackleve text(128),producpacknum text(128),groupsetid text(128),groupitemid text(128),producompany text(128),bidcomany text(128),groupsetname text(128),groupitemname text(128),speci text(128),model text(128),perforcompo text(128),packspeci text(128),packmatel text(128),brand text(128),unit text(128),winbidprice text(128),cate text(128),a text(128));'
        conn.execute(sql)
    
    
    def save_sqlite(self, items):
        conn = sqlite3.connect('drug.db')
        cure = conn.cursor()
        cure.executemany(
            'INSERT INTO info(catenname, packname, producpackleve, producpacknum, groupsetid,groupitemid,producompany) VALUES (?,?,?,?,?,?,?)',
            items)
        conn.commit()
        conn.close()


    

    def main(self):
        # self.create_db()
        city = self.getCityUrl(self.url_city)
        print("总共有%d个城市" % len(city))
        s = 1
        s1 = 0
        for site in city:
            hossite = self.getHosUrl(site)
            print("第%d个城市共有%d个医院" % (s,len(hossite)) )
            for sites in hossite[2331:]:
                data = self.getHosDate(sites)
                if len(data) == 1:
                    self.save_sqlite(data)
                    print(sites)
                else:
                    print(sites)
                    print("页面404 忽略")
                s1 += 1
                time.sleep(1)
                print("正在保存第%d个城市的第%d个医院" % (s,s1))
                print(sites)
            s += 1
        # data = self.getHosDate("http://yyk.99.com.cn/zhixia/106287/")
        # print(data)

    def get_city(self):
        self.create_db()
        s = 1
        hossite = self.getHosUrl("http://yyk.99.com.cn/shandong/")
        print("总共有%d家医院" % len(hossite))
        for sites in hossite:
            data = self.getHosDate(sites)
            if len(data) == 1:
                self.save_sqlite(data)
            else:
                print(sites)
                print("页面404 忽略")
            print("正在保存第%d个医院" % (s))
            time.sleep(1)
            print(sites)
            s += 1
         
h = Hospital()
h.get_city()