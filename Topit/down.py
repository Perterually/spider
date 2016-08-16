# -*- coding:utf-8 -*-
# py3
from urllib.parse import urlencode

import requests
from bs4 import BeautifulSoup

from Topit.seting import *


class TopIt():
    def __init__(self):
        self.urls = 'http://www.topit.me/event/warmup/welcome/views/index.html'

        self.session = requests.Session()
        self.session.headers.update(Head)

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
        self.session.get(self.urls)
        re = self.session.get(url, headers=Heads)
        return re.content.decode('utf-8')

    # 返回一页的链接
    def get_item_url(self, index):
        li = []
        date = self.get_page(index)
        bs = BeautifulSoup(date, 'lxml')
        for tag in bs.find_all('div', class_='catalog'):
            for link in tag.find_all('a',target='_blank'):
                url = link.get('href')
                li.append(url)
        return li

t = TopIt()
s = t.get_item_url(1)
print(s)
