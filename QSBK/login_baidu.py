# -*- coding:utf-8 -*-
import cookielib
import urllib
import urllib2

loginSite = 'https://passport.baidu.com/v2/api/?login'

cj = cookielib.CookieJar()
cookie_suppor = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_suppor, urllib2.HTTPHandler)
urllib2.install_opener(opener)

postdate = {'staticpage': 'http://tieba.baidu.com/tb/static-common/html/pass/v3Jump.html',
            'charset': 'GBK',
            'token': '6060f4034e07a300b51bdd05ad395344',
            'tpl': 'tb',
            'apiver': 'v3',
            'tt': '1460687830190',
            'safeflg': '0',
            'u': 'http://tieba.baidu.com/',
            'isPhone': 'false',
            'detect': '1',
            'gid': '587CDBE-0AE9-4E0B-8739-D34A5CC9BEF0',
            'quick_user': '0',
            'logintype': 'dialogLogin',
            'logLoginType': 'pc_loginDialog',
            'loginmerge': 'true',
            'splogin': 'rate',
            'username': '376974004',
            'password': 'QQm5aM+lQ0xyAk+7GzfSEKHjSCWoflw54riOxtDIrCU2xvFAm8PqBLyFIzbTerWj8+MZiDVqdt3Ct50LmiBVBE8bY8cVyX4jx/r4nt2CayXqFuv5k6ldKuoGToK7N7539mMLC4UE82H63jW48DAzXaZHKyxkhdxxDD+Z3WPU8g==',
            'mem_pass': 'on',
            'rsakey': 'AWR5Z0wze2K2lIUWKMG4RXa7qCslF7Gv',
            'crypttype': '12',
            'ppui_logintime': '26499',
            'callback': 'parent.bd__pcbs__robrsc'}

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
header = {'User-Agent': user_agent}
postDate = urllib.urlencode(postdate)

request = urllib2.Request(loginSite, postDate, headers=header)
reponse = urllib2.urlopen(request)
print reponse.read()
