import requests
import os
from bs4 import BeautifulSoup

# 爬取目标
url = 'http://www.mzitu.com/page/'
parser = 'html.parser'
cur_path = os.getcwd() +'/妹子图' + '/'


# print(cur_path)
# 设置报头，Http协议
#header = {'User-Agent': 'Mozilla'}
header = { "Accept":"text/html,application/xhtml+xml,application/xml;",
            "Accept-Encoding":"gzip",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Referer":"http://www.baidu.com/",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
            }

#header = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
# 爬取的预览页面数量
preview_page_cnt = 1
for cur_page in range(1, int(preview_page_cnt) + 1):
    cur_url = url + str(cur_page)
    cur_page = requests.get(cur_url, headers=header)
    # 解析网页
    soup = BeautifulSoup(cur_page.text, parser) #解析首页
    # 图片入口和文字入口取一个即可
    preview_tag_list = soup.find(id='pins').find_all('a', target='_blank')[1::2] #找到所有的满足条件的a标签
    for tag in preview_tag_list:
        dir_name = tag.get_text().strip().replace('?', '') #strip() 移除空格
        link = tag['href'] #
        soup = BeautifulSoup(requests.get(link).text, parser) #解析首页的页面
        # 获取图片数量 <a href='http://www.mzitu.com/101826/46'><span>46</span></a> 第4个a标签中存储着尾页信息
        pic_cnt = soup.find('div', class_='pagenavi').find_all('a')[4].get_text() #因为class是关键字所以加'_'
        # 创建目录
        pic_path = cur_path + dir_name
        if os.path.exists(pic_path):
            print('directory exist!')
        else:
            os.mkdir(pic_path)
        os.chdir(pic_path)  # 进入目录，开始下载
        print('下载' + ":" + dir_name + '...')
        # 遍历获取每页图片的地址
        for pic_index in range(1, int(pic_cnt) + 1):
            pic_link = link + '/' + str(pic_index)
            cur_page = requests.get(pic_link, headers=header)
            soup = BeautifulSoup(cur_page.text, parser)
            pic_src = soup.find('div', 'main-image').find('img')['src'] #找到图片链接 "http://i.meizitu.net/2017/09/01b01.jpg"
            pic_name = pic_src.split('/')[-1] #找到图片名字，链接的最后一个字符串 ---.jpg
            f = open(pic_name, 'wb')
            f.write(requests.get(pic_src, headers=header).content)
            f.close()
        os.chdir(cur_path)  # 完成下载，退出目录
print('下载完成')