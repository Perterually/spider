# -*- coding:utf-8 -*-

import cookielib
import urllib
import urllib2


class babyBook():
    def login(self):
        loginsite = 'http://www.baobaobooks.com/user.php?act=signin'

        # 获取一个cookie容器
        cj = cookielib.CookieJar()
        # cookier容器与http处理器绑定
        cookie_suppor = urllib2.HTTPCookieProcessor(cj)
        #
        opener = urllib2.build_opener(cookie_suppor, urllib2.HTTPHandler)
        urllib2.install_opener(opener)

        postdata = {'username': '376974004@qq.com',
                    'password': '13831016530',
                    }
        user_agent = 'ozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
        header = {'User-Agent': user_agent}
        postData = urllib.urlencode(postdata)

        request = urllib2.Request(loginsite, postData, header)
        reponse = urllib2.urlopen(request)
        return reponse.read()

    def getUser(self, paperSite):
        self.login()
        request = urllib2.Request(paperSite)
        reponse = urllib2.urlopen(request)
        print reponse.read()


bb = babyBook()
bb.getUser('http://www.baobaobooks.com/user.php')
