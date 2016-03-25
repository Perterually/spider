#-*- coding:utf-8 -*-
import MySQLdb
import urllib
import urllib2
import re
import MySQLdb

class QSBK(object):

    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)'
        self.headers = {'User-Agent':self.user_agent}
        #初始化heades
        self.stories = []
        self.enable = True
    def getPage(self,pageIndex):
        url = 'http://www.qiushibaike.com/8hr/page/' + str(pageIndex)
        request = urllib2.Request(url,headers = self.headers)
        reponse = urllib2.urlopen(request)
        content =  reponse.read().decode('utf-8')
        return content
    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print '页面加在失败'
            return None
        pattern = re.compile('<div.*?clearfix">.*?<h2>(.*?)</h2>.*?<div.*?content">(.*?)<!.*?>',re.S)
        items = re.findall(pattern,pageCode)
        pageDate = []
        for item in items:
            #过滤掉不需要的信息
            replaceBR = re.compile('<br/>')
            text = re.sub(replaceBR,'\n',item[1])
            pageDate.append([item[0].strip(),text.strip()])
        return pageDate
    def instertDB(self,pageIndex):
            qsbk = self.getPageItems(pageIndex)
            #插入数据到mysql数据库
            conn = MySQLdb.connect('172.19.1.213','root','root','text')
            cur = conn.cursor()
            cur.executemany('insert into spider (name,text) value (%s,%s);',qsbk)

            conn.commit()
            conn.close()
a = QSBK()
a.instertDB(1)