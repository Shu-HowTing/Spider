# -*- coding: utf-8 -*-
# Author: 小狼狗

# 导入 webdriver
from selenium import webdriver

# 调用环境变量指定的PhantomJS浏览器创建浏览器对象
driver = webdriver.PhantomJS()

# 如果没有在环境变量指定PhantomJS位置
#driver = webdriver.PhantomJS(executable_path=r"C:\Program Files\phantomjs\bin\phantomjs")

# get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
driver.get("http://www.baidu.com/")

# 获取页面名为 wrapper的id标签的文本内容
data = driver.find_element_by_id("wrapper").text

# 打印数据内容
#print data

# 打印页面标题 "百度一下，你就知道"
print(driver.title)