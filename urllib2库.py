# -*- coding: utf-8 -*-
# Author: 小狼狗

# 导入urllib2 库
#import urllib2    #python2
import urllib.request as ur  #在python3中，urllib2 被改为 urllib.request
import random
import urllib
import requests
import json


# # 向指定的url发送请求，并返回服务器响应的类文件对象
# response = ur.urlopen("http://www.baidu.com")
# # 类文件对象支持 文件对象的操作方法，如read()方法读取文件全部内容，返回字符串
# html = response.read()
# # 打印字符串
# print(html)
#
# #-----------------------------------------------------------------------------------
# '''
# 如果需要执行更复杂的操作，比如增加HTTP报头，必须创建一个 Request 实例来作为urlopen()的参数；
# 而需要访问的url地址则作为 Request 实例的参数。
# '''
# # url 作为Request()方法的参数，构造并返回一个Request对象
# # 反爬的第一步
# ua_list = ["Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
#            "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
#            "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)",
#            "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11"]
# user_agent = random.choice(ua_list)
# request = ur.Request("http://www.baidu.com/s?wd=%E5%8D%8E%E5%8D%97%E7%90%86%E5%B7%A5")
#
# #可以通过调用Request.add_header() 添加/修改一个特定的header
# request.add_header("User-Agent", user_agent)
#
# # 也可以通过调用Request.get_header()来查看header信息
# #注意：header_name的首字母必须大写，其他字母小写;
# print(request.get_header(header_name = "User-agent"))
#
# # Request对象作为urlopen()方法的参数，发送给服务器并接收响应
# response = ur.urlopen(request)
#
# html = response.read().decode('utf-8')
# #返回响应状态码
# print(response.getcode())  #200
# print(html) # 结果是一样的
#
# url = "http://www.baidu.com/s?"
# keyword = input("请输入你想要查询的内容：")
# wd = {'wd':keyword}
# wd = urllib.parse.urlencode(wd) #
# full_url = url + wd
# req = ur.Request(full_url)
# req.add_header("User-Agent", user_agent)
#
# html = ur.urlopen(req).read().decode('utf-8')
# print(html)
#---------------------------------------------------------------
#POST请求方法
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc"
key = input("请输入你要查询的单词：")
form_data = {
            "type": "AUTO",
            "i": key,
            "doctype": "json",
            "xmlVersion": "1.8",
            "keyfrom": "fanyi.web",
            "ue": "UTF-8",
            "action": "FY_BY_CLICKBUTTON",
            "typoResult": "true"
            }

header = {
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "X-Requested-With":"XMLHttpRequest"
    }
data = urllib.parse.urlencode(form_data).encode(encoding='utf-8') #POST的数据必须是byte
request = ur.Request(url, data=data, headers=header)
response = ur.urlopen(request).read().decode('utf-8')  #解码成str
content = json.loads(response)
print(content["translateResult"][0][0]['tgt'])  # 被封了^-^
#
# #*--------------------------------------------------------------------------------------------*
# '''
# 自定义opener：
#     opener是 urllib2.OpenerDirector 的实例，我们之前一直都在使用的urlopen，它是一个特殊的opener（也就是模块帮我们构建好的）。
#     但是基本的urlopen()方法不支持代理、cookie等其他的HTTP/HTTPS高级功能。所以要支持这些功能：
#         使用相关的 Handler处理器 来创建特定功能的处理器对象；
#         然后通过 urllib2.build_opener()方法使用这些处理器对象，创建自定义opener对象；
#         使用自定义的opener对象，调用open()方法发送请求。
#         如果程序里所有的请求都使用自定义的opener，可以使用urllib2.install_opener() 将自定义的opener对象定义为全局opener，
#         表示如果之后凡是调用urlopen，都将使用这个opener*（根据自己的需求来选择）
# '''
# #构建一个HTTP处理器对象，支持处理HTTP的请求
# http_handler = ur.HTTPHandler()
#
# ## 调用urllib2.build_opener()方法，创建支持处理HTTP请求的opener对象
# opener = ur.build_opener(http_handler)
#
# request = ur.Request("http://www.baidu.com/")
#
# response = opener.open(request)
#
# print(response.read().decode('utf-8'))

#*--------------------------------------------------------------------------------------------*
'''
ProxyHandler处理器(代理设置)：

    使用代理IP，这是爬虫/反爬虫的第二大招，通常也是最好用的。

    很多网站会检测某一段时间某个IP的访问次数(通过流量统计，系统日志等)，如果访问次数多的不像正常人，它会禁止这个IP的访问。

    所以我们可以设置一些代理服务器，每隔一段时间换一个代理，就算IP被禁止，依然可以换个IP继续爬取。

    urllib2中通过ProxyHandler来设置使用代理服务器，下面代码说明如何使用自定义opener来使用代理：
'''
#{"http":"59.173.75.48:808"}

#代理开关,决定是否用代理
proxy_switch = True

if proxy_switch:
    ## 构建了代理Handler，有代理IP
    http_proxy = ur.ProxyHandler({"https":"119.29.18.239:8888"})
else:
    http_proxy = ur.ProxyHandler({})

opener = ur.build_opener(http_proxy)

url = "http://www.baidu.com/"

request = ur.Request(url)

response = opener.open(request)

print(response.read().decode('utf-8'))

#私密代理
username = "***"
passwd = "***"

http_proxy = ur.ProxyHandler({"https":"username:passwd@119.29.18.239:8888"})

opener = ur.build_opener(http_proxy)

url = "http://www.baidu.com/"

request = ur.Request(url)

response = opener.open(request)

print(response.read().decode('utf-8'))


