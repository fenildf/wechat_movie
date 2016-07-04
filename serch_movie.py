# -*- coding:utf-8 -*-
# import urllib2
# from lxml import html
import requests
from bs4 import BeautifulSoup

def serch_movie(movie_name):
    key = {'wp': '0', 'ty': 'gn', 'op': 'gn', 'q': movie_name, 'q': movie_name}
    r = requests.get('http://www.wangpansou.cn/s.php', params=key)
    soup = BeautifulSoup(r.text, "html.parser")
    urls = soup.find_all("a", attrs={"class": "cse-search-result_content_item_top_a"})
    if len(urls) > 3:
        movie_url = "网盘地址："+'1.'+urls[0].get('href')+'\n2.'+urls[1].get('href')+'\n3.'+urls[2].get('href')
    else:
        movie_url = "网盘地址："+'1.'+urls[0].get('href')
    return movie_url

