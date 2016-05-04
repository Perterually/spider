# -*- coding:utf-8 -*-
import urllib2
from pyquery import PyQuery as pq

from bs4 import BeautifulSoup


class Into:
    def __init__(self):
        self.url = 'http://mobile.gyb365.com/guarder/getDurgInstructions?productID=22718116-6368-FE10-E050-10AC02016A78&drugName=%E5%AE%89%E5%90%96%E5%95%B6%E6%B3%A8%E5%B0%84%E6%B6%B2'

    def get_page(self, url):
        reponse = urllib2.Request(url)
        request = urllib2.urlopen(reponse)
        return request.read()

    def get_info(self):
        source = self.get_page(self.url)
        pagedate = BeautifulSoup(source, 'lxml')
        tag = pagedate.find('ul',id='drugmanual')
        for nav in tag('p'):
            print nav.text

i = Into()
i.get_info()
