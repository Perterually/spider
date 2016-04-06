#-*- coding:utf-8 -*-
import urllib
import urllib2
import re
import os
import tool
'''
#一个简单的图片爬虫
'''
class TBMM():
    def __init__(self):
        self.pageIndex = 1
        self.tool = tool.Tool()
        self.pageSite = []
        self.pageImg = []
        self.enable = True
    #页面入口
    def getPage(self,pageIndex):
        url = "https://mm.taobao.com/json/request_top_list.htm" + "?page=" + str(pageIndex)
        requset = urllib2.Request(url)
        reponse = urllib2.urlopen(requset)
        content = reponse.read().decode('gbk')
        return content

    #获取数据
    def getDate(self,pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile('<div.*?pic s60">.*?<a href=".*?".*?<img src="(.*?)".*?<.*?class="lady-name" href="(.*?)".*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
        items = re.findall(pattern,page)
        pageDate = []
        for item in items:
            #替换//
            replacell = re.compile('//')
            replacells = re.compile('model_card.htm')
            replaceafter = re.sub(replacell,'https://',item[0])
            # replaceafters = re.sub(replacell,'http://',item[0])
            replaceafterss = re.sub(replacell,'https://',item[1])
            #替换信息
            replaceafterssInfo = re.sub(replacells,'info/model_info_show.htm',replaceafterss.strip())
            pageDate.append([replaceafter.strip(),replaceafterssInfo.strip(),item[2],item[3],item[4]])
        return pageDate


    #获取页面函数
    def getMmSite(self,infoURl):
        reponse = urllib2.urlopen(infoURl)
        contenxt = reponse.read().decode('gbk')
        return contenxt


    #获取个人图片所在地址
    def getmmImgInfoSite(self,infoSite):
        page = self.getMmSite(infoSite)
        pattern = re.compile('<span>(.*?)</span>.*?<span>(.*?)</span>.*?<span>(.*?)</span>.*?<span>(.*?)</span>.*?<span>(.*?)</span>.*?<span>(.*?)</span>.*?<span>(.*?)</span>.*?<span>(.*?)</span>.*?<span>(.*?)</span>.*?<span>(.*?)</span>',re.S)
        result = re.findall(pattern,page)
        for item in result:
            relacell = re.compile('//')
            replaceafter = re.sub(relacell,'http://',item[9])
            self.pageSite.append(replaceafter)
        return self.pageSite

    #获取页面所有图片链接
    def getmmImgSite(self,page):
        getmmImg = self.getMmSite(page)
        pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
        # items = re.findall(pattern,getmmImg)
        # print items
        content = re.search(pattern,getmmImg)
        #获取图片自己
        patternImg = re.compile('<img.*?src="(.*?)"',re.S)
        imageWeb = re.findall(patternImg,content.group(0))
        list = []
        for site in imageWeb:
            self.pageImg.append(site)
        # del self.pageImg[0]
        return self.pageImg
    #获取个人信息
    def getmInfo(self,page):
        getmmImg = self.getMmSite(page)
        pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
        result = re.search(pattern,getmmImg)
        return self.tool.replace(result.group(0))

    #创建文件夹
    def mkdir(self,path):
        path = str(path)
        status = os.path.exists(path)
        if not status:
            print u'创建名字叫做',path,u'的文件夹'
            os.makedirs(path)
        else:
            print u'文件夹',path,u'已经存在'
            return False

    #保存图片方法
    def saveImg(self,imgUrl,name):
        u = urllib.urlopen(imgUrl)
        data = u.read()
        f = open(name, 'wb')
        f.write(data)
        print u'保存图片为',name
        f.close()
    #读取一页链接
    def loadPageSite(self,pageIndex):
        if self.enable == True:
            contents = self.getDate(pageIndex)
            if contents:
                for item in contents:
                    inforurl = item[1]
                    getmm = self.getMmSite(inforurl)
                    imgSite = self.getmmImgInfoSite(getmm)
                return imgSite

    #调用getmmImgSite函数 获取页面所有链接
    def pageAllImg(self):
        for i in self.pageSite:
            return self.getmmImgSite(i)

    #list操作
    def replayll(self):
        items = []
        for item in self.pageAllImg():
            items.append([item])
        return items

    #list 操作
    def cycleSite(self):
        items = []
        for item in self.replayll():
            items.append(item)
        return items

    #list 操作
    def replaySite(self):
        items = []
        for item in self.cycleSite():
            pattern = re.compile('//')
            replary = re.sub(pattern,'http://',item[0])
            items.append(replary)
        return items

    #循环保存图片
    def saveImgAll(self,imgImtem,name):
        number = 1
        print u'发现第',name,u'个人共有',len(imgImtem),u'张照片'
        for imageUrl in imgImtem:
            fileName = str(name) + '/' + str(number) + '.' + 'jpg'
            self.saveImg(imageUrl,fileName)
            number += 1

    #保存一页人的图所有片
    def savePageInfo(self,pageIndex):
        num = 1
        contents = self.getDate(pageIndex)
        for item in contents:
            infoSite = item[1]
            self.getmmImgInfoSite(infoSite)
            imgSite = self.replaySite()
            self.mkdir(num)
            self.saveImgAll(imgSite,num)
            num += 1
        self.pageSite = []
    #传入起至页
    def savePages(self,start,end):
        for i in range(start,end+1):
            print u'正在保存第%d' % i + u'页照片'
            self.savePageInfo(i)
mm = TBMM()
mm.savePages(1,3)