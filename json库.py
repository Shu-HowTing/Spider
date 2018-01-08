# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
JSON:

    json简单说就是javascript中的对象和数组，所以这两种结构就是对象和数组两种结构，通过这两种结构可以表示各种复杂的结构
        对象：对象在js中表示为{ }括起来的内容，数据结构为 { key：value, key：value, ... }的键值对的结构，
        在面向对象的语言中，key为对象的属性，value为对应的属性值，所以很容易理解，取值方法为 对象.key 获取属性值，
        这个属性值的类型可以是数字、字符串、数组、对象这几种。

        数组：数组在js中是中括号[ ]括起来的内容，数据结构为 ["Python", "javascript", "C++", ...]，
        取值方式和所有语言中一样，使用索引获取，字段值的类型可以是 数字、字符串、数组、对象几种。
'''
import json
import jsonpath
import requests
url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"
header = {
    "User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
    }
response = requests.get(url, headers = header)

#把Json格式字符串解码转换成Python对象
js = json.loads(response.text)  #type：dic

# #通过python的字典取值
# cities = js["content"]["data"]["allCitySearchLabels"]
# for i in range(65, 92):
#     x = cities[chr(i)]
#     city = [i["name"] for i in x]
#     print(city)

#通过jsonpath进行解析
city_list = jsonpath.jsonpath(js,'$..name')

#print(type(city_list))

# 将Python内置类型序列化为json对象后写入文件
# dumps默认中文编码是ascii,禁用之后，返回Unicode编码
content = json.dumps(city_list, ensure_ascii=False)

with open('city.js','wb') as fp:
    fp.write(content.encode('utf-8'))
