import requests
# """
# get方法：
#     r = requests.get(url)
#     requests.get(url)构造一个Request对象（向服务器请求资源的对象）
#     返回一个Response对象，包含以下常用属性：
#        r.status_code：返回请求状态，200表示链接成功
#        r.text：http响应内容的字符串形式，即url对应页面的内容
#        r.content：http响应内容的二进制格式
# """
# r = requests.get("http://www.baidu.com")
# print(r.status_code)
# print(r.text)
# r.encoding = 'utf-8'
# print(r.text)

#通用框架
# def getHTML_Text(url):
#     try:
#         r = requests.get(url)
#         r.raise_for_status()  #如果不是200，则引发HTTPError
#         r.encoding = r.apparent_encoding
#         print(r.text)
#     except:
#         print("请求出错！")
# if __name__ == '__main__' :
#     url = "http://www.baidu.com"
#     getHTML_Text(url)

#ronots协议 亚马逊商品的查询

# r = requests.get("https://www.amazon.cn/gp/product/B07477ZM7J")
# r.encoding = r.apparent_encoding
# print(r.text)
# print(r.request.headers)
# kv = {'User-Agent':'Mozilla'}
#
# try:
#     r = requests.get("https://www.amazon.cn/gp/product/B07477ZM7J", headers=kv)
#     r.raise_for_status()
#     r.encoding = r.apparent_encoding
#     print(r.text[1000:2000])
# except:
#     print("error")
#
# #通过百度关键字搜索 wd = "..."
# keyword = "python"
#
# try:
#     kv = {'wd':keyword}
#     r = requests.get("http://www.baidu.com/s", params=kv)
#     r.raise_for_status()
#     print(r.request.url)  #http://www.baidu.com/s?wd=python
#     print(len(r.text))
# except:
#     print("Error")

# url = "http://img0.dili360.com/rw9/ga/M00/48/B6/wKgBzFmRaUGABgI1AEKmnaEYc_o074.tub.jpg"
# path = "./abc.jpg"
# try:
#     r = requests.get(url)
#     r.raise_for_status()
#     with open(path,'wb') as f:
#         f.write(r.content)
# except:
#     print("Error")
#
#查询IP地址
try:
    kv = {'ip':'202.204.80.112'}
    r = requests.get("http://m.ip138.com/ip.asp", params=kv)
    r.raise_for_status()
    print(r.request.url)  #http://www.baidu.com/s?wd=python
    print(r.text[-500:])
except:
    print("Error")

#--------------------------------------------------------------------------------------
'''
requests的POST方法
'''

key = input("请输入你要查询的单词：")
form_data = {
    "type":"AUTO",
    "i":key,
    "doctype":"json",
    "xmlVersion":"1.8",
    "keyfrom":"fanyi.web",
    "ue":"UTF-8",
    "action":"FY_BY_ENTER",
    "typoResult":"true"
}

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

response = requests.post(url, data = form_data, headers = headers)


# 如果是json文件可以直接显示
print(response.json()["translateResult"][0][0]['tgt'])
