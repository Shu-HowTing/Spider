# -*- coding: utf-8 -*-
# Author: 小狼狗
import requests
import os
import re
from json import loads
from bs4 import BeautifulSoup
# #
# # 爬取目标
# url = 'https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8'
# parser = 'html.parser'
#
#
# header = { "Accept":"text/html,application/xhtml+xml,application/xml;",
#             "Accept-Encoding":"gzip",
#             "Accept-Language":"zh-CN,zh;q=0.8",
#             "Referer":"http://www.baidu.com/",
#             "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
#             }
# html = requests.get(url, headers=header)
# js = html.text
# dict = loads(js)
# info = dict['data']['searchDOList']
# for i in info:
#     print(i['userId'])
Cookie = 'SINAGLOBAL=6549936336494.185.1502082889334; ' \
         'UM_distinctid=15e1df4dabe1167-0d4d619398d677-17c153c-144000-15e1df4dac2ceb; wvr=6;' \
         'YF-Ugrow-G0=9642b0b34b4c0d569ed7a372f8823a8e; ' \
         'login_sid_t=dd1d49617b655d433fcc07a563af12e6; ' \
         'cross_origin_proto=SSL; YF-V5-G0=46bd339a785d24c3e8d7cfb275d14258; ' \
         'WBStorage=c1cc464166ad44dc|undefined; _s_tentry=passport.weibo.com; ' \
         'Apache=7327651088415.222.1514713926657; ' \
         'ULV=1514713926669:66:11:1:7327651088415.222.1514713926657:1514625287194; ' \
         'SCF=Ar65IdkbvlSobIGeaYSSS_v3SYboLh9nzNWtsGgZ0REy4IM30KTo2H0u5xP2niT5bOCyQ9FfJHtOIqjcM8ol8Ns.; ' \
         'SUB=_2A253TMMIDeRhGeNI61US9y7OzDiIHXVUO7PArDV8PUNbmtBeLU_bkW9NSLlNnDyPAwDO5l6ZBWiK0U-C3nSOKuon; ' \
         'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWATJVHT6uJUqlswzsEvhR15JpX5KzhUgL.Fo-cehM0S05ES0B2dJLoIp7LxKqLB-BLBKBLxKML1KBL1-qLxKML1hnLBo81; ' \
         'SUHB=00xpCYcTDuapBH; ALF=1546249943; SSOLoginState=1514713944; wb_cusLike_5607370274=Y; ' \
         'YF-Page-G0=0acee381afd48776ab7a56bd67c2e7ac; UOR=www.techweb.com.cn,widget.weibo.com,www.baidu.com'
# get your cookie from Chrome or Firefox
header = {
        'Accept': '* / *',
        #'Accept - Encoding':'gzip, deflate, sdch, br',
        'Accept - Language':'zh - CN, zh;q = 0.8',
        'Connection':'keep - alive',
        'Content - Type':'application / x - www - form - urlencoded',
        #'Host':'weibo.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
        'Cookie': Cookie
       }


def visit():
    url = 'https://weibo.com/'
    r = requests.get(url, headers = header)
    r.encoding = r.apparent_encoding
    html = r.text

    # print the title, check if you login to weibo sucessfully
    soup = BeautifulSoup(html,'html.parser')

    divs = soup.find_all('div', class_="WB_info")
    print(divs)
    for div in divs:
        a = div.find_all('a',class_='W_f14 W_fb S_txt1').get_text()
        print(a)

if __name__ == '__main__':
    visit()