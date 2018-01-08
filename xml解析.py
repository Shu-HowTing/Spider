# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
    熟悉xml文件的解析
'''
#解析xml文件
from lxml import etree
import requests


X = etree.parse('./books.xml')
print(type(X))
# selector = etree.XML(X)
#获取所有的 <book> 标签
h1 =  X.xpath('/bookstore/book')    #返回list
print(h1)                     #列表中是Element对象
print(etree.tostring(h1[0]))  #显示标签的具体内容


#获取<book>标签的所有category属性值
h2 = X.xpath('/bookstore/book/@category')
print(h2)  #['children', 'cooking', 'web', 'web']

#获取<book>标签下lang="en"的<title>标签
h3 = X.xpath('/bookstore/book/title[@lang="en"]')
print(etree.tostring(h3[0]))

#获取lang="en"的所有标签
h4 = X.xpath('/bookstore//*[@lang="en"]')
print(etree.tostring(h4[0]))

#获取<title>标签的内容
h5 = X.xpath('/bookstore//title/text()')
print(h5)   #['Harry Potter', 'Everyday Italian', 'Learning XML', 'XQuery Kick Start']

#条件筛选
l = X.xpath('/bookstore/book[price>29]/title/text()')
for x in l:
    print(x)

#-----------------------------------------------------------------------------------
#解析网页
url = "https://python123.io/ws/demo.html"
'''
<html>
    <head>
        <title>This is a python demo page</title>
    </head>
    <body>
        <p class="title"><b>The demo python introduces several python courses.</b></p>
        <p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
            <a href="http://www.icourse163.org/course/BIT-268001" class="py1" id="link1">Basic Python</a> and
            <a href="http://www.icourse163.org/course/BIT-1001870001" class="py2" id="link2">Advanced Python</a>.
        </p>
    </body>
</html>
'''

r = requests.get(url)
#lxml解析
selector = etree.HTML(r.text)
l = selector.xpath('//a/text()')#返回list
print(l)
