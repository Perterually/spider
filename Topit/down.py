# -*- coding:utf-8 -*-
# py3
from urllib.parse import urlencode

import requests

from Topit.seting import *


class TopIt():
    def __init__(self):
        self.urls = 'http://www.topit.me/event/warmup/welcome/views/index.html'

        self.session = requests.Session()
        self.session.headers.update(Head)

    @staticmethod
    def index_url(self, index):
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


t = TopIt()
s = t.index_url(1)
print(s)
