# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup


class DataJson():
    def __init__(self):
        self.prueinfo = []

    # 返回每一个药品的id和药品名字
    def get_id_name(self, data):
        list = []
        data_data = data['data']
        drugList = data_data['drugList']
        for d in drugList:
            # d['productDrugID'], d['showName']
            list.append([d['productDrugID'], d['showName']])
        return list

    # 返回一个药品ID下的所有厂家的信息
    def get_into(self, jsondata, prim):
        list = []
        try:
            data = jsondata['data']
            drugData = data['drugData']
            drugList = drugData['drugList']
            for prueinto in drugList:
                list.append(
                    [prueinto['productDrugID'], prueinto['showName'], prueinto['drugSpec'], prueinto['factory'], prim])
        except Exception, ex:
            print Exception, ':', ex
        return list

    # 返回药品名字和id
    def get_id(self, data):
        list = []
        data_data = data['data']
        drugList = data_data['drugList']
        for d in drugList:
            # d['productDrugID'], d['showName']
            list.append(d['productDrugID'])
        return list


   #返回一个药品的厂家的所有id
    def get_drug_id(self,jsondata):
        list = []
        try:
            data = jsondata['data']
            drugData = data['drugData']
            drugList = drugData['drugList']
            for prueinto in drugList:
                list.append(
                    [prueinto['productDrugID'],prueinto['showName']])
        except Exception, ex:
            print Exception, ':', ex
        return list

