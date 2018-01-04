# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
CSS选择器
    这就是另一种与 find_all 方法有异曲同工之妙的查找方法.
    写 CSS 时，标签名不加任何修饰，类名前加 . ，id名前加 #
    在这里我们也可以利用类似的方法来筛选元素，用到的方法是 soup.select()，返回类型是 list
'''
import re
import requests
from bs4 import BeautifulSoup
r = requests.get("http://python123.io/ws/demo.html")
soup = BeautifulSoup(r.text, 'lxml')  #注意解析器是 'lxml'
#按照标签名选择标签，返回一个列表
l1 = soup.select('p')
print(l1)
#通过类名查找
l2 = soup.select('.title')
print(l2)
#通过id名查找
l3 = soup.select('#link1')
print(l3)   #[]
#组合查找
l4 = soup.select('p.title')
print(l4)
###注意比较
l5 = soup.select('p .title')
print(l5) # []
l6 = soup.select('p #link1') #[<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>]
print(l6)
#####区别：
    #如果没有空格，则属性和标签属于同一节点，即l4查找的是'class = title'的p标签
    #而如果加上空格，则属性和标签不属于同一节点，即l5查找的是p标签下'class = title'的标签
#直接子标签查找，则使用 > 分隔 , 注意 > 左右的空格一定有
l7 = soup.select('p > a')
print(l7)
#按照属性查找
l8 = soup.select('p[class="course"]')
print(l8)
#查找p下 id = 'link1'的标签
l9 = soup.select('p [id="link1"]')
print(l9)
#获取内容
#以上的 select 方法返回的结果都是列表形式，可以遍历形式输出，
# 然后用 get_text() 方法来获取它的内容
for l in l9:
    print(l.get('href'))  #http://www.icourse163.org/course/BIT-268001
    print(l.get_text())   #Basic Python