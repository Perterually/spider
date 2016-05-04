# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
import json
import time
import urllib2


class Drug:
    def __init__(self):
        self.pruename = []
        self.enable = True
        self.url = 'http://mobile.gyb365.com/guarder/Controller/MicroMessage/drugSearch'
        self.content = 'application/json;charset=UTF-8'
        self.headers = {'Content-Type': self.content}

    #  Get data of the paper is json  type is dict
    def get_page_date(self, pageIndex):
        postdate = '{"search":"","page":"%d","count":"30"}' % pageIndex
        request = urllib2.Request(self.url, postdate, headers=self.headers)
        f = urllib2.urlopen(request)
        content = f.read()
        contenty = json.loads(content)
        return contenty

    #


    # Get productDrugID and showName
    def get_name_id(self, data):

        data_data = data['data']
        drugList = data_data['drugList']
        for d in drugList:
            # d['productDrugID'], d['showName']
            self.pruename.append(d['productDrugID'])
        return (self.pruename)




    # Control paper
    def get_all_date(self):
        paper = 1
        while self.enable:
            data = self.get_page_date(paper)
            paper += 1
            time.sleep(2)
            print self.get_name_id(data)


d = Drug()
d.get_all_date()
