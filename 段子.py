# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
    使用正则爬取内涵段子上的段子
'''
import re
import urllib.request as urllib2

class Duanzi():
    def __init__(self):
        self.page = 1
        self.switch = True

    def load_Page(self):
        """
            @brief 定义一个url请求网页的方法
            @param page 需要请求的第几页
            @returns 返回的页面html
        """
        print("正在爬取第{}页····".format(self.page))
        url = " http://www.neihan8.com/article/list_5_" + str(self.page) + ".html"
        header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"}
        request = urllib2.Request(url, headers=header)
        html = urllib2.urlopen(request).read().decode('gbk')
        #print(html)
        self.deal_page(html)


    def deal_page(self, html):
        '''
        :param html: 获得的网页
        从获得的网页中提取段子，并进行相关处理
        '''
        pattern = re.compile(r'<div.*?class="f18 mb20">(.*?)</div>', re.S)
        item_list = pattern.findall(html)
        print("正在保存第{}页····".format(self.page))
        #对文字进行处理，删除无用的标记
        for item in item_list:
            item = item.replace("<p>", "").replace("</p>", "").replace("<br />", "")
            self.write_page(item)

    def write_page(self, item):

        with open("joke.txt", "a") as f:
            f.write(item.strip()+'\n')

    def work_do(self):
        """
        控制爬虫的运行
        """
        while self.switch:
            self.load_Page()
            command = input("是否继续爬取(y/n):")
            if command == 'n':
                self.switch = False

            else:
                self.page += 1
        print("谢谢使用！")
if __name__ == '__main__':
    duanziSpider = Duanzi()
    duanziSpider.work_do()