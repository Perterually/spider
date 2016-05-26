# -*- coding:utf-8 -*-
import json
import time
import urllib2

import prue_info


class Drug:
    def __init__(self):
        self.prueinfo = prue_info.PrueInfo()
        self.pruename = []
        self.enable = True
        self.url = 'http://mobile.gyb365.com/guarder/Controller/MicroMessage/drugSearch'
        self.content = 'application/json;charset=UTF-8'
        self.headers = {'Content-Type': self.content}

    def get_page_date(self, pageIndex):
        if pageIndex:
            postdate = '{"search":"","page":"%d","count":"30"}' % pageIndex
            request = urllib2.Request(self.url, postdate, headers=self.headers)
            f = urllib2.urlopen(request)
            content = f.read()
            contenty = json.loads(content)
            durglist = contenty['data']
            if int(durglist['stateCode']) == 200 and durglist['drugList'] == []:
                print '数据收集完成'
                return
            else:
                print durglist



    def get_name_id(self, data):
        data_data = data['data']
        drugList = data_data['drugList']
        for d in drugList:
            # d['productDrugID'], d['showName']
            self.pruename.append(d['productDrugID'])
        return self.pruename

    def get_all_date(self):
        paper = 1
        while self.enable:
            data = self.get_page_date(paper)
            paper += 1
            time.sleep(5)
            prueitem = self.get_name_id(data)
            print prueitem
            self.prueinfo.get_prueinfoinserdb(prueitem)
            self.pruename = []
            print u'正在保存第%d页' % paper


            # 最大页数608



d = Drug()
d.get_all_date()
