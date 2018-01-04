import re
import requests
from bs4 import BeautifulSoup

#url = 'https://s.taobao.com/search?q=书包'
def getHTMLText(url):
    r = requests.get(url)
    try:
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def parsePage(lst, html):
    try:
        plt = re.findall(r'"view_price":"\d.*?"', html)
        tlt = re.findall(r'"raw_title":".*?"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1]) #eval 去除冒号
            title = eval(tlt[i].split(':')[1])
            lst.append([price, title])
    except:
        print("!!!!")


def printGoodList(infoList):
    tplt = '{0:4}\t{1:8}\t{2:16}'
    print(tplt.format("序号", "价格", "商品名称"))   #表头
    count = 0
    for g in infoList:
        count += 1
        print(tplt.format(count, g[0], g[1]))

def main():
    goods = '书包'
    depth = 3
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodList(infoList)

main()




