# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup


class Detail:
    def get_guide_span(self, content):
        list = []
        source = BeautifulSoup(content, 'lxml')
        tag = source.find(id='drugguide')
        try:
            for s in tag.find_all('span'):
                list.append(s.string.encode('utf-8'))
        except Exception, ex:
            print Exception, ':', ex
        return list

    def get_guide_li(self, content):
        list = []
        source = BeautifulSoup(content, 'lxml')
        tag = source.find(id='drugguide')
        try:
            for s in tag.find_all('ol'):
                list.append(s.get_text().encode('utf-8'))
        except Exception, ex:
            print Exception, ':', ex
        return list

    # 返回名称
    def get_span(self, content):
        list = []
        source = BeautifulSoup(content, 'lxml')
        tag = source.find(id='drugmanual')
        try:
            for s in tag.find_all('span'):
                list.append(s.string.encode('utf-8'))
            return list
        except Exception, ex:
            print Exception, ':', ex

    # 返回信息
    def get_p(self, content):
        list = []
        source = BeautifulSoup(content, 'lxml')
        tag = source.find(id='drugmanual')
        try:
            for s in tag.find_all('p'):
                list.append(s.get_text().encode('utf-8'))
            return list
        except Exception, ex:
            return list
            print Exception, ':', ex

    # 返回说明书的list
    def get_drug_use(self, content):
        list = []
        span = self.get_span(content)
        p = self.get_p(content)
        try:
            for row in range(len(span)):
                list.append([span[row], p[row]])
        except Exception, ex:
            print Exception, ':', ex
        return list

    # 返回指导的list
    def get_drug_guidet(self, content):
        list = []

        span = self.get_guide_span(content)
        li = self.get_guide_li(content)
        try:
            for row in range(len(span)):
                list.append([span[row], li[row]])
        except Exception, ex:
            print Exception, ':', ex
        return list

    def get_drug_dict(self, content):
        span = self.get_span(content)
        p = self.get_p(content)
        try:
            s = dict(zip(span, p))
            return s
        except Exception, ex:
            print Exception, ':', ex

    def get_drug_use_dict(self, content):
        span = self.get_guide_span(content)
        p = self.get_guide_li(content)
        try:
            s = dict(zip(span, p))
            return s
        except Exception, ex:
            print Exception, ':', ex
