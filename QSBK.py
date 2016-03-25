# -*- coding:utf-8 -*-
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
    def loadPage(self):
        if self.enable == True:
            pageStories = self.getPageItems(self.pageIndex)
            if pageStories:
                self.stories.append(pageStories)
                self.pageIndex += 1

    def getOneStory(self,stories,page):
        for story in stories:
            input = raw_input()
            self.loadPage()
            if input == 'q':
                self.enable = False
                return
            print u"第%d条\t发布人:%s\n发布内容:%s" %(page,story[0],story[1])
    def start(self):
        print u"正在读取糗事百科,按回车查看新段子，Q退出"
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories)>0:
                pageStoried = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getOneStory(pageStoried,nowPage)
            else:
                return
a = QSBK()
a.start()