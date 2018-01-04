# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
    熟悉xml文件的解析
'''
#解析xml文件
from lxml import etree
import requests
url = "https://python123.io/ws/demo.html"

X = etree.parse('./books.xml')
print(type(X))
# selector = etree.XML(X)
h =  X.xpath('/bookstore/book/price/text()')    #返回list

print(h)

l = X.xpath('/bookstore/book[price>29][1]/title/text()')
for x in l:
    print(x)


r = requests.get(url)

#lxml解析
selector = etree.HTML(r.text)
l = selector.xpath('//p/text()') #返回list
print(l)
