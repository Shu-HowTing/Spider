# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
 调用cookielib保存网页请求的cookie，进而访问已经登陆的网站
'''
import urllib
import urllib.request as urllib2
import http.cookiejar

# 1. 构建一个CookieJar对象实例来保存cookie
# py2的写法：import cookielib ; cookie = cookielib.CookieJar()
cookie = http.cookiejar.CookieJar()

# 2. 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
cookie_handler = urllib2.HTTPCookieProcessor(cookie)

# 3. 通过 build_opener() 来构建opener
opener = urllib2.build_opener(cookie_handler)

# 4. addheaders 接受一个列表，里面每个元素都是一个headers信息的元祖, opener将附带headers信息
opener.addheaders = [("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36")]


url = "http://www.renren.com/PLogin.do"

# 5. 需要登录的账户和密码
data = {"email":"1549189937@qq.com", "password":"1549189937"}

# 6. 通过urlencode()转码
data = urllib.parse.urlencode(data).encode(encoding='utf-8')

# 7. 构建Request请求对象，包含需要发送的用户名和密码
req = urllib2.Request(url, data=data)

# 8. 通过opener发送这个请求，并获取登录后的Cookie值，
response = opener.open(req)

print(response.read().decode('utf-8'))
print("*"*80)

# 9. opener包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
response1 = opener.open("http://www.renren.com/389014096/profile")
print(response1.read().decode('utf-8'))