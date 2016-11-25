from urllib.parse import urlencode

import requests


class Login:
    def __init__(self):
        self.head = {
            'Host': 'www.baobaobooks.com',
            'Origin': 'ttps://www.baobaobooks.com',
            'Referer': 'https://www.baobaobooks.com/user.php',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'
        }
        self.session = requests.Session()
        self.session.headers.update(self.head)
        self.postdata = {
            'username': '376974004@qq.com',
            'password': '13831016530',
            'back_act': './index.php'
        }
        self.param = {
            'act': 'signin'
        }
        self.url = 'https://www.baobaobooks.com/user.php?'
        self.urls = 'https://www.baobaobooks.com/user.php?act=order_list'

    def get_url(self):
        url = self.url + urlencode(self.param)
        return url

    def login(self):
        url = self.get_url()
        self.session.post(url, self.postdata)
        rs = self.session.get(self.urls)
        print(rs.text)


l = Login()
l.login()
