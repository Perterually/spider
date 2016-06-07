# -*- coding:utf-8 -*-
import json
import urllib2

from bs4 import BeautifulSoup


class demo:
    def __init__(self):
        self.drug_use_url = 'http://mobile.gyb365.com/guarder/getDurgInstructions?'
        self.content = 'application/json;charset=UTF-8'
        self.headers = {'Content-Type': self.content}
        self.productID = 'productID='
        self.drugName = '&drugName='

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

    def get_text(self):
        list = []
        content = self.get_drup_detail('2D8462EA-4877-477B-8505-719212ECD222', '氨酪酸注射液')
        source = BeautifulSoup(content, 'lxml')
        tag = source.find(id='drugmanual')
        for s in tag.find_all('li'):
            list.append(s.get_text())
        print list

    def get_drup_detail(self, productId, drugName):
        url = self.drug_use_url + self.productID + productId + self.drugName + drugName
        print url
        request = urllib2.Request(url)
        reponse = urllib2.urlopen(request)
        return reponse.read()


d = demo()
d.get_text()
