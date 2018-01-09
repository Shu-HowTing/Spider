# -*- coding: utf-8 -*-
# Author: 小狼狗

import unittest
from selenium import webdriver
from bs4 import BeautifulSoup

class Douyu(unittest.TestCase):
    #初始化方法
    def setUp(self):
        #创建一个PhantomJS浏览器对象
        self.driver = webdriver.PhantomJS()

    #测试方法，必须有test字样开头
    def testDouyu(self):
        while True:
            #获取网页
            self.driver.get(url= "https://www.douyu.com/directory/all" )
            #解析网页
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            names = soup.find_all('span', {"class": "dy-name ellipsis fl"})
            numbers = soup.find_all('span', {"class": "dy-num fr"})
            links = soup.find_all('a', {"class" : "play-list-link"})
            #打印输出
            for name, number, link in zip(names, numbers, links):
                print("观众人数:" + number.get_text() + "\t房间号:" + name.get_text() + "\t链接:" + \
                                                   "https://www.douyu.com" + link.get('href'))
            #判断是否到了最后一页
            if self.driver.page_source.find("shark-pager-disable-next") != -1:
                break
            #返回的是一个列表，注意从中取值
            self.driver.find_elements_by_class_name("shark-pager-next")[0].click()

    #定义测试结束要执行的操作
    def tearDown(self):
        #退出PhantomJS浏览器
        self.driver.quit()

if __name__ == '__main__':
    #启动测试模块
    unittest.main()