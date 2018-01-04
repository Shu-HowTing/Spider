import requests
import re
from bs4 import BeautifulSoup
r = requests.get("http://python123.io/ws/demo.html")
#HTML文件格式
demo = r.text
print(demo)
soup = BeautifulSoup(demo, 'html.parser')
# # print(soup.title)
# tag = soup.a
# # print(tag.name)
# print(tag.attrs)
# # #下行遍历
# # print(soup.body.contents[3])
# # print(soup.head.contents)
# # #上行遍历
# # parents = soup.a.parents
# # for parent in parents:
# #     if parent is None:
# #         print(parent)
# #     else:
# #         print(parent.name)
# # #平行遍历
# # print(soup.a.next_sibling)  # and
# # #格式化显示
# # print(soup.prettify())
for link in soup.find_all('a'):
#     #print(link.get('href'))
#     print(link.attrs['href']
    print(link['href'])
#
# #HTML的内容查找方法
# #find_all
# print(soup.find_all('a')) #返回一个列表
# print(soup.find_all(['a', 'b']))
# #找到所有标签
# #print(soup.find_all(True))
# print(soup.find_all('a', class_='py1'))
print(soup.find_all('a')) #等价于
print(soup('a'))
# # #不精确查找
# # print(soup.find_all('a', string = re.compile('Python')))
# # print(soup.find_all(id='link1'))
#
# url = "https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html"
# header = {'User-Agent':
#         'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
#          }
# data = requests.get(url=url, headers=header)
# soup = BeautifulSoup(data.text, 'lxml')
# images = soup.select('div.prw_rup.prw_common_centered_thumbnail > div > div > img')
# for i in images:
#     print(i.get('src'))














