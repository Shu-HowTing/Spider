# 目标：
# 1.巩固之前工具的使用：seletom动态执行，bs4选择节点，requests请求页面
# 2.可以通过输入url，爬取知乎网任意一个问题下的回答中，所有的图片
# 3.爬取下来的图片，会统一存在一个以该问题命名的文件夹下，并命名为答主的ID

# 目前问题：知乎新版的页面，是动态解析的，所以只能在滑动到页面底部的时候，才会加载全部内容
# 没有滑动到的图片都显示的是<noscript>标签
# 更多button只有在滑倒到底部的时候，才会点击有效

# 所以最大的问题是如何判断页面已经滑动到底部了

# 如果不能代码判断，那就只好硬等了，在每次滑动页面执行后，等待60秒，确保到达页面底部，然后点击继续

# -*- coding:utf-8 -*-
# 使得python支持中文

import requests
from requests.exceptions import MissingSchema
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import os
import time

class ZHGP:
    # 初始化
    def __init__(self):
        pass
    # 让界面滚动到底部的函数
    def scroll(self,driver):
        driver.execute_script("""
            (function () {
                var y = document.body.scrollTop;
                var step = 100;
                window.scroll(0, y);


                function f() {
                    if (y < document.body.scrollHeight) {
                        y += step;
                        window.scroll(0, y);
                        setTimeout(f, 50);
                    }
                    else {
                        window.scroll(0, y);
                        document.title += "scroll-done";
                    }
                }
                setTimeout(f, 1000);
            })();
            """)

        # 开始爬取
    def beginSpider(self,url):

        # 1. 前期工作
        driver = webdriver.Chrome('C:\Google\Chrome\Application\chromedriver.exe')
        driver.get(url)
        x = driver.get_cookies()
        driver.add_cookie({'name': 'nweb_qa', 'value': 'heifetz'})
        driver.refresh()
        try:
            # 首先加载出全部的内容，判断是否页面中存在“更多”这一个按钮
            while True:
                # 这里需要注意的是：selenium2 是不支持类名之中有空格的
                try:
                    self.scroll(driver)
                    time.sleep(60)
                    more = driver.find_element_by_css_selector("button.Button.QuestionMainAction")
                    actions = ActionChains(driver)
                    actions.move_to_element(more)
                    actions.click(more)
                    actions.perform()
                    # more.click() # 如果我们在页面中找到了更多，那么就点击更多，然后等两秒
                except NoSuchElementException as e:
                    break
            # 加载了全部的内容后，获取到所有内容，存为items
            soup = BeautifulSoup(driver.page_source,"html.parser")
            # 2. 对soup进行操作，获取出title，和包含内容的列表items
            titles = soup.find("title").text.replace('\n', '').replace('?', '').split()
            title = titles[0]
            print(title)
            # 如果当前目录下没有title命名的文件夹，则创建一个
            dirpath = os.getcwd() + "\\妹子图\\" + title + "\\"
            if not os.path.exists(dirpath):
                os.makedirs(dirpath)

            items = soup.find_all("div", class_=re.compile("List-item"))
            nimingCount = 0
            for item in items:
                # 分为两种情况：1.匿名用户，没有第一张头像 2. 匿名用户有第一张头像
                userName = item.find('img', class_="Avatar AuthorInfo-avatar").get("alt")
                if "匿名" in userName:
                    userName = "匿名用户_" + str(nimingCount)
                    nimingCount += 1
                count = 0  # 一个用户下有多个照片的
                images = item.find_all('img',class_ = "origin_image zh-lightbox-thumb lazy")

                for image in images:
                    # 保存图片
                    imageSrc = image.get("src")
                    picName = dirpath + userName + '_' + str(count) + ".jpg"
                    count += 1

                    try:
                        imageData = requests.get(imageSrc, stream=True).content
                        try:
                            with open(picName, 'wb') as jpg:
                                jpg.write(imageData)
                        except IOError as e:
                            print(userName + "的一张图片写入错误")
                    except MissingSchema as e:
                        print(userName + "的一张图片获取失败")
                        print("地址为：" + imageSrc)
        finally:
            # 最后要记得关闭浏览器，否则就会永远开着
            driver.quit()

zhgp = ZHGP()
#zhgp.beginSpider("https://www.zhihu.com/question/28521492")
zhgp.beginSpider("https://www.zhihu.com/question/31839156")