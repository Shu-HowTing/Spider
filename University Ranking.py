import requests
import bs4
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        demo = r.text
        #soup = BeautifulSoup(demo, "html.parser")
    except:
        print("Error")
    return demo

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:  #找到所有的tr标签，每一个tr标签对应一个大学的所有信息
        if isinstance(tr, bs4.element.Tag): #判断tr是否是bs4.element.Tag标签类型
            tds = tr('td')  #找出tr标签中的所有td标签，返回的是list格式
            ulist.append([tds[0].string, tds[1].string, tds[3].string])

def printUnivList(ulist, num):
    tplt = '{0:^10}\t{1:{3}^10}\t{2:^10}'  #^10居中对齐，占10个位置。不够时用中文字符填充 chr(12288)
    print(tplt.format("排名", "学校名称", "分数", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))

def main():
    ulist = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)
    fillUnivList(ulist, html)
    printUnivList(ulist, 22)   #打印前22个学校的排名

main()