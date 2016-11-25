# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json
import re



class VideoUrl:
    def __init__(self):
        self.url = "http://pl.hd.sohu.com/videolist?playlistid=5036614&o_playlistId=&vid=745234&pianhua=0&pageRule=undefined&pagesize=999&order=0&cnt=1&callback=__get_videolist"
    
    def get_url(self):
        data =requests.get(self.url)
        
        pattent = re.compile(r'\w')
        items = re.match(pattent,data)
        print(items.group())
      

v = VideoUrl()
v.get_url()
