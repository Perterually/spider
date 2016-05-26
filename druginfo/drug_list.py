# -*- coding:utf-8 -*-
import json
import sys
import urllib2

from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf8')


class DrugList():
    def __init__(self):
        self.drug_list_url = 'http://mobile.gyb365.com/guarder/Controller/MicroMessage/drugSearch'
        self.drug_info_url = 'http://mobile.gyb365.com/guarder/Controller/MicroMessage/drugSearchMore'
        self.drug_use_url = 'http://mobile.gyb365.com/guarder/getDurgInstructions?'
        self.productID = 'productID='
        self.drugName = '&drugName='
        self.content = 'application/json;charset=UTF-8'
        self.headers = {'Content-Type': self.content}
        self.errorid = []

    # 获取一页的药品名称和ID的json
    def get_paper_data(self, pageIndex):
        if pageIndex:
            postdate = '{"search":"","page":"%d","count":"30"}' % pageIndex
            request = urllib2.Request(self.drug_list_url, postdate, headers=self.headers)
            f = urllib2.urlopen(request)
            content = f.read()
            contenty = json.loads(content)
            durglist = contenty['data']
            if int(durglist['stateCode']) == 200 and durglist['drugList'] == []:
                print '数据收集完成,出现没有药品详细的id是',self.errorid
                return
            else:
                return contenty

    # 根据药品id获取每个id下的所有生产厂家的所生产的药品的信息json
    def get_drup_data(self, prueid):
        postdate = '{"productDrugID":"%s"}' % prueid
        request = urllib2.Request(self.drug_info_url, postdate, headers=self.headers)
        data = urllib2.urlopen(request)
        data_json = data.read()
        read_json = json.loads(data_json)
        if read_json['result'] == 500:
            self.errorid.append([prueid])
        elif read_json['result'] == 0:
            self.errorid.append([prueid])
        else:
            return read_json

    # 获取使用说明和指导的页面
    def get_drup_detail(self, productId,drugName):
        url = self.drug_use_url + self.productID + productId + self.drugName + drugName
        print url
        request = urllib2.Request(url)
        try:
            reponse = urllib2.urlopen(request)
            return reponse.read()
        except Exception,ex:
            print Exception,ex

    # 返回errorid
    def get_errorid(self):
        print self.errorid

    # 返回指导页面的方法
    def get_drup_detal_data(self, data):
        list = []
        date = data['data']
        drugData = date['drugData']
        drugList = drugData['drugList']
        for d in drugList:
            # d['productDrugID'], d['showName']
            return self.get_drup_detail(d['productDrugID'], d['showName'])
    # 返回名称
    def get_span(self):
        list = []
        content = self.get_page()
        source = BeautifulSoup(content, 'lxml')
        tag = source.find(id='drugmanual')
        for s in tag.find_all('span'):
            list.append(s.string)
        return list

    # 返回信息
    def get_p(self):
        list = []
        content = self.get_page()
        source = BeautifulSoup(content, 'lxml')
        tag = source.find(id='drugmanual')
        for s in tag.find_all('p'):
            list.append(s.get_text())
        return list

    # 返回
    def get_drug_use(self):
        list = []
        span = self.get_span()
        p = self.get_p()
        for row in range(len(span)):
            list.append([span[row], p[row]])
        print list
