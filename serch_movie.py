# -*- coding:utf-8 -*-
import urllib2
from lxml import etree
def serch_movie(movie_name):
    url = 'http://www.wangpansou.cn/s.php?wp=0&ty=gn&op=gn&q=%s&q=%s' % (movie_name, movie_name)
    print(url)
    headers = {
                'Connection': 'keep-alive',
                'Accept': 'image/webp,image/*,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.8',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36',
                'Referer': url
    }
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    html_content = etree.HTML(content)
    movie_url_path = '//*[@id="cse-search-result"]/div[5]/table/tbody/tr/td/div[1]/a'
    movie_url = html_content.xpath(movie_url_path)
    return movie_url

if __name__ == '__main__':
    url = serch_movie('x战警')
    print(url
          )