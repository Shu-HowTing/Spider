from bs4 import BeautifulSoup
# l = [1,2,3,4,5,6,7]
# print(l[1::2])
# demo = '<a class="bets-name" href="/stock/sh201000.html">\n         R003 (<span>201000</span>)\n            </a>'
# soup = BeautifulSoup(demo, 'html.parser')
# a = soup.find_all('a', class_="bets-name" )[0]
# print(a)
# name = a.get_text()
# print(name)
# #print(name.split('(')[0].strip())
# print(a.text.split()[0])
# # print(type(name))
# s = '23'
# print(s)
# a = int(s)
# print(a)
# print(type(a))
#
# A = {'b':45.0}
# q = 'a'
# price = '2.00'
# if q not in A:
#     A[q] = float(price)
# print(A)
#
# x = soup.find('c')
# print(x)
#
# # -*- coding: utf-8 -*-
# n = raw_input()
# A = raw_input()
# a = []
# for i in A.split(' '):
#   a.append(int(i))
#
# b = []
# c = []
# for i in range(len(a)):
#     for j in range(len(a)):
#         if i != j:
#             b.append([a[i],a[j]])
#
# for i in range(len(b)):
#     x1, x2 = b[i]
#     x2 = str(x2)
#     x = x1*(10**len(x2)) + int(x2)
#     if x % 7 == 0:
#         c.append(x)
# print c
# print len(c)

#即诶下xml文件
from lxml import etree
import requests
X = etree.parse('./books.xml')
# print(type(X))
# # selector = etree.XML(X)
# h =  X.xpath('/bookstore/book/price/text()')    #返回list
#
# l = X.xpath('/bookstore/book[price>29][1]/title/text()')
# for x in l:
#     print(x)
#
url = "https://python123.io/ws/demo.html"
#r = requests.get(url)

r = requests.get(url)
#BeautifulSoup解析
#soup = BeautifulSoup(r.text,'lxml')
#print(soup)

#lxml解析
selector = etree.HTML(r.text)
l = selector.xpath('//p/text()')
print(l)








