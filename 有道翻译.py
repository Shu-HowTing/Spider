# -*- coding: utf-8 -*-
# Author: 小狼狗
import urllib.request as urllib2  #在python3中，urllib2 被改为 urllib.request
import random
import urllib
import requests
import json
import hashlib
import time

def createData(transStr):
    '''
    待翻译的内容
    :param transStr:
    :return: dict
    '''
    salt = str(int(time.time() * 1000))
    client = 'fanyideskweb'
    a = 'rY0D^0\'nM0}g5Mm1z%1G4'

    #获取sign
    sign = hashlib.md5((client + transStr + salt + a).encode('utf-8')).hexdigest()

    #POST的数据
    data = {
            'i': transStr ,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,
            'sign': sign,
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_ENTER',
            'typoResult': 'true'
            }
    return data

def translation(form_data):
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict2.top"
    header = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
            }

    # data = urllib.parse.urlencode(form_data).encode(encoding='utf-8') #POST的数据必须是byte
    # request = urllib2.Request(url, data=data, headers=header)
    # response = urllib2.urlopen(request).read().decode('utf-8')  #解码成str
    response = requests.post(url, form_data, headers = header)
    #讲js转换成dic

    content = json.loads(response.text)
    #print(type(response.text))
    return content["translateResult"][0][0]['tgt']

if __name__=='__main__':
    key = input("请输入你要查询的单词：")
    form_data = createData(key)
    result = translation(form_data)
    print(result)


