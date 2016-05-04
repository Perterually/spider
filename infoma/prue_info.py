# -*- coding:utf-8 -*-
import json
import urllib2


class PrueInfo:
    def __init__(self):
        self.headers = {'Content-Type': self.content}
        self.url = 'http://mobile.gyb365.com/guarder/Controller/MicroMessage/drugSearchMore'

    # return prue infomation
    def get_paper(self, prueid, ):
        postdate = '{"productDrugID":"%d"}' % prueid
        request = urllib2.Request(self.url, postdate, headers=self.headers)
        data = urllib2.urlopen(request)
        data_json = data.read()
        read_json = json.loads(data_json)
        return read_json
    #Control the output list ID
    def