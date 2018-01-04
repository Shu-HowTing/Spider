# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
===============================================================
动态数据：
    随着滚轮的滑动，自动加载一些数据；而不是通过点击“下一页”加载；
    此时，页面的链接是不会改变的，如何爬取网站的而数据？
===============================================================
'''

import time
import requests
from bs4 import BeautifulSoup


header = { "Accept":"text/html,application/xhtml+xml,application/xml;",
            "Accept-Encoding":"gzip",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Referer":"http://www.baidu.com/",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
            }

def getHTMLText(url):
    r = requests.get(url, headers=header)
    try:
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def parsePage(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        imgs = soup.select('a.cover-inner > img')
        titles = soup.select('section.content > h4 > a')
        links = soup.select('section.content > h4 > a')
        for img, title, link in zip(imgs, titles, links):
            data = {
                    "img" : img.get('src'),
                    "title": title.get('title'),
                    "link": link.get('href')
                  }
            print(data)
    except:
        print("!!!!")

def get_page(base_url, start, end):
    for one in range(start, end):
        url = base_url + str(one)
        #time.sleep(2)
        html = getHTMLText(url)
        parsePage(html)

if __name__ == '__main__':
    base_url = 'https://knewone.com/discover?page='
    get_page(base_url, 1, 10)
