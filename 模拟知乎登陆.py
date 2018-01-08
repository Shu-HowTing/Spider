# -*- coding: utf-8 -*-
# Author: 小狼狗
import requests
import re
'''
    利用cookie模拟登陆知乎
'''


# # #设置头信息
# headers_base = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     #'Accept-Encoding': 'gzip, deflate, sdch',
#     'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
#     'Connection': 'keep-alive',
#     'Host': 'www.zhihu.com',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
#     'Referer': 'http://www.zhihu.com/',
# }
#
# def getContent(url):
#     #使用requests.get获取知乎首页的内容
#     r = requests.get(url, headers=headers_base)
#     #request.get().content是爬到的网页的全部内容
#     return r.text
#
# #获取_xsrf标签的值
# def getXSRF(url):
#     #获取知乎首页的内容
#     content = getContent(url)
#     #正则表达式的匹配模式
#     pattern = re.compile('.*?<input type="hidden" name="_xsrf" value="(.*?)"/>.*?')
#
#     match = re.findall(pattern, content)
#     xsrf = match[0]
#     print(xsrf)
#     #返回_xsrf的值
#     return xsrf
#
# #登录的主方法
# def login(baseurl, email, password):
#     #post需要的表单数据，类型为字典
#     login_data = {
#             '_xsrf': getXSRF(baseurl),
#             'password': password,
#             'remember_me': 'true',
#             'email': email,
#     }
#
#
#     #使用seesion登录，这样的好处是可以在接下来的访问中可以保留登录信息
#     session = requests.session()
#     #登录的URL
#     baseurl += "/login/email"
#     #requests 的session登录，以post方式，参数分别为url、headers、data
#     content = session.post(baseurl, headers = headers_base, data = login_data)
#    #成功登录后输出为 {"r":0,
#     #"msg": "\u767b\u9646\u6210\u529f"
#      #}
#     #print (content.text)
#     #注：登录失败，要输入验证码
#     #再次使用session以get去访问知乎首页，一定要设置verify = False，否则会访问失败
#     s = session.get("https://www.zhihu.com", verify = False)
#     tree = html.fromstring(s.text)
#     # #print(tree)
#     topic = tree.findall(".//div[@class='Card TopstoryItem']//a/text()")
#     for i in topic:
#         print(i)
#
# url = "https://www.zhihu.com"
# #进行登录，将星号替换成你的知乎登录邮箱和密码即可
# login(url,"1549189937@qq.com","1234qwer")
#-------------------------------------------------------------------------------------------
'''
    利用request创建session会话，并将cookie保存到本地，进行提交登陆。
        1. 抓包工具获取登陆需要POST数据：email/password/_xsrf/captcha
        2. 获取_xsrf
        3. 获取captcha(验证码)，保存到本地，手动输入
        4. session.post()进行登陆
        5. 将cookie信息保存到本地
注意：知乎改版，本方法已经不适用，不再是获得_xsrf验证，而是通过signature验证
'''
import time
from http import cookiejar
import requests
from bs4 import BeautifulSoup

headers = {
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87'
}




# 使用登录cookie信息
session = requests.session()
session.cookies = cookiejar.LWPCookieJar(filename='cookies.txt')
try:
    print(session.cookies)
    session.cookies.load(ignore_discard=True)

except:
    print("还没有cookie信息")


def get_xsrf():
    '''
    获得网站的xsrf：作用是防止CSRF(跨站请求伪造)，又叫跨域攻击。
    :return:
    '''
    response = session.get("https://www.zhihu.com", headers=headers, verify=False)
    soup = BeautifulSoup(response.content, "html.parser")
    xsrf = soup.find('input', attrs={"name": "_xsrf"}).get("value")
    return xsrf


def get_captcha():
    """
    把验证码图片保存到当前目录，手动识别验证码
    :return:captcha
    """
    t = str(int(time.time() * 1000))
    captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
    print(captcha_url)
    r = session.get(captcha_url, headers=headers)
    with open('captcha.jpg', 'wb') as f:
        f.write(r.content)
    captcha = input("验证码：")
    return captcha


def log_in(email, password):
    login_url = 'https://www.zhihu.com/login/email'
    #登陆需要提交的数据
    data = {
            'email': email,
            'password': password,
            '_xsrf': get_xsrf(),
            "captcha": get_captcha(),
            'remember_me': 'true'
          }

    response = session.post(login_url, data=data, headers=headers)

    #保存cookie
    session.cookies.save()

    #显示登陆成功反馈信息
    login_code = response.json()
    print(login_code['msg'])  #登录成功
    #print(session.cookies)

    #从登录成功的网站进一步点击其他网站进行验证
    r = session.get("https://www.zhihu.com/settings/profile", headers=headers)
    #保存个人的设置页面
    with open("my.html", "wb") as f:
        f.write(r.content)


if __name__ == '__main__':
    email = "1549189937@qq.com"
    password = "dsh1549189937"
    log_in(email, password)
    #json_str = ""