'''
    爬取妹子图首页模特的图片
'''
import os
import requests
import random
from bs4 import BeautifulSoup

# 爬取目标
url = 'http://www.mzitu.com/page/'
parser = 'html.parser'
cur_path = os.getcwd() +'/妹子图' + '/'

# 随机获取headers
user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" \
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]
header = {
            "Referer":'http://meizitu.com',
            "User-Agent": random.choice(user_agent_list)
         }

# 爬取的预览页面数量
preview_page_cnt = 1

for cur_page in range(1, int(preview_page_cnt) + 1):
    cur_url = url + str(cur_page)
    cur_page = requests.get(cur_url, headers=header)
    # 解析妹子图首页
    soup = BeautifulSoup(cur_page.text, parser)
    # 图片入口和文字入口取一个即可
    preview_tag_list = soup.find(id='pins').find_all('a', target='_blank')[1::2] #找到所有的满足条件的a标签
    for tag in preview_tag_list:
        dir_name = tag.get_text().strip().replace('?', '') #strip() 移除空格
        #获取首页上每一个妹子入口链接
        link = tag['href']
        soup = BeautifulSoup(requests.get(link, headers=header).text, parser) #解析首页的页面
        # 获取每一个妹子图片数量  第4个a标签中存储着尾页信息
        pic_cnt = soup.find('div', {'class':'pagenavi'}).find_all('a')[4].get_text()
        # 为每一个妹子创建一个目录
        pic_path = cur_path + dir_name
        if os.path.exists(pic_path):
            print('directory exist!')
        else:
            os.makedirs(pic_path)
        # 进入目录，开始下载
        os.chdir(pic_path)
        print('下载' + ":" + dir_name + '...')
        # 获取每张高清图片的地址
        for pic_index in range(1, int(pic_cnt) + 1):
            #每一张预览图片的链接
            pic_link = link + '/' + str(pic_index)
            cur_page = requests.get(pic_link, headers=header)
            soup = BeautifulSoup(cur_page.text, parser)
            #获取每一张原图的链接  "http://i.meizitu.net/2017/09/01b01.jpg"
            pic_src = soup.find('div', 'main-image').find('img')['src']
            # 找到图片名字，链接的最后一个字符串 ***.jpg
            pic_name = pic_src.split('/')[-1]
            with open(pic_name, 'wb') as f :
                f.write(requests.get(pic_src, headers=header).content)
        os.chdir(cur_path)  # 完成下载，退出目录
print('下载完成')