# -*- coding:utf-8 -*-
import re
import urllib2

from bs4 import BeautifulSoup

'''获取所有城市的当前环境数据'''


class PM():
    def __init__(self):
        self.url = 'http://pm25.in'

    # 获取页面的方法
    def getPageDate(self, site):
        request = urllib2.Request(site)
        response = urllib2.urlopen(request)
        return response.read().decode('utf-8')

    # 获取城市的链接
    def getCity(self):
        cityList = []
        source = self.getPageDate(self.url)
        data = BeautifulSoup(source, 'lxml')
        for tag in data.find_all(class_='unstyled'):
            for link in tag.find_all('a'):
                site = link.get('href')
                pattern = re.compile('^/\w+')
                item = re.findall(pattern, site)
                if item:
                    citySite = self.url + item[0]
                    cityList.append(citySite)
        # 去除重复元素
        cityList = list(set(cityList))
        return cityList

    # 获取一个城市的环境数据
    def getCityDate(self, site):
        source = self.getPageDate(site)
        print source
        # pattern = re.compile('<div class="city_name">.*?<h2>(.*?)</h2>')
        # item = re.findall(pattern, source)
        # print item

    # 获取所有城市的数据
    def getAllDate(self, cityList):
        data = self.getCityDate(cityList)


pm = PM()