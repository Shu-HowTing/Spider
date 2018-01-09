# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
    学会pytesseract库的使用，并尝试识别知乎的登录验证码
'''

import time
import requests
from pytesseract import image_to_string
from PIL import Image

# image = Image.open('test1.jpg')
# text = image_to_string(image)
# print(text)

def get_captcha():
    """
    把验证码图片保存到当前目录，自动识别验证码
    :return:captcha
    """
    headers = {
        "Host": "www.zhihu.com",
        "Referer": "https://www.zhihu.com/",
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87'
    }
    #获取验证码的链接
    t = str(int(time.time() * 1000))
    captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
    r = requests.get(captcha_url, headers=headers)

    #将验证码保存到本地
    with open('captcha.jpg', 'wb') as f:
        f.write(r.content)

    #return captcha

if __name__ == '__main__':
    get_captcha()
    image = Image.open('captcha.jpg')
    text = image_to_string(image)
    print(text)