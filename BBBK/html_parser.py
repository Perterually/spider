# -*- coding:utf-8 -*-
import re
import urlparse

from bs4 import BeautifulSoup
from pyquery import PyQuery as pq


class HtmlParser():
    pass

    def get_new_urls(self, pagaurl, soup):
        new_urls = set()

        liks = soup.find_all('a', href=re.compile(r"/view/47200.htm"))

        for link in liks:
            new_url = link['href']
            new_full_url = urlparse.urljoin(pagaurl, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def get_new_data(self, paga_url, soup):
        res_data = {}
        res_data['url'] = paga_url
        # <dd class="lemmaWgt-lemmaTitle-title">
        title_note = soup.find('dd', class_='lemmaWgt-lemmaTitle-title'.find('h1'))
        res_data['title'] = title_note.get_text()

        summary_note = soup.find('div', class_='<div class="lemma-summary"')
        res_data['summary'] = summary_note.get_text()
        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        # else:
        #     soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        #     new_urls = self.get_new_urls(page_url, soup)
        #     new_data = self.get_new_data(page_url, soup)
        #     print new_data
        #     return new_urls, new_data
        else:
            source = pq()
