# -*- coding:utf-8 -*-
# py3
from urllib.parse import urlencode

import requests
from bs4 import BeautifulSoup

from Topit.seting import *


class TopIt():
    def __init__(self):
        self.urls = 'http://www.topit.me/event/warmup/welcome/views/index.html'
        self.url = 'http://www.topit.me/'
        self.session = requests.Session()
        self.session.headers.update(Head)
        self.session.get(self.urls)

    @staticmethod
    def index_url(index):
        url = 'http://www.topit.me/'
        param = {
            'p': index
        }
        return url + '?' + urlencode(param)

    # 返回一页的数据
    def get_page(self, index):
        url = self.index_url(index)
        # self.session.get(self.urls)
        re = self.session.get(url, headers=Heads)
        return re.content.decode('utf-8')

    # 返回一页的链接
    def get_item_url(self, index):
        li = []
        date = self.get_page(index)
        bs = BeautifulSoup(date, 'lxml')
        for tag in bs.find_all('div', class_='catalog'):
            for link in tag.find_all('a', target='_blank'):
                url = link.get('href')
                li.append(url)
        return li

    # 返回图片地址
    def get_jpg_url(self, url):
        s = self.session.get(url, headers=Heads)
        for i in s.cookies.iteritems():
            cooki = dict(PHPSESSID=i[1])
        rs = self.session.get(url, headers=Heads, cookies=cooki)
        date = rs.text
        bs = BeautifulSoup(date, 'lxml')
        for tag in bs.find_all('div', style='padding-top: 5px;'):
            for a in tag.find_all('a'):
                link = a.get('href')
                return link


t = TopIt()
s = t.get_jpg_url('http://www.topit.me/item/18435592')
print(s)
