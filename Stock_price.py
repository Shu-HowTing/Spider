import re
import requests
from bs4 import BeautifulSoup

def getHTMLText(url, code = 'utf-8'):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        print("...")

#从东方财富网获取股票的代码
def getStockList(stock_url, lst):
    #东方财富网的编码是GB2312
    demo = getHTMLText(stock_url, code='GB2312')
    soup = BeautifulSoup(demo, 'html.parser')
    a = soup.find_all('a', target='_blank')
    for i in a[83:200]: #调式发现，所需要的证券代码每次都从列表的第83个位置开始（上一句寻找a标签有待修改），所以这里偷个懒。。。。
        try:
            href = i['href']
            stock_num = re.findall(r'[s][hz]\d{6}', href)
            lst.append(stock_num)
        except:
            continue

#从百度股票上获取当时股票的价格
def getStockInfo(url, s_list, file_path):
    count = 0
    for stock_num in s_list:
        infoDict = {}
        stock_url = url + 'stock/' + str(stock_num[0]) + '.html'
        demo = getHTMLText(stock_url)
        try:
            if demo == "":
                continue
            soup = BeautifulSoup(demo, 'html.parser')
            strong = soup.find_all('strong', class_="_close")
            price = strong[0].get_text()
            a = soup.find_all('a', class_="bets-name")
            name = a[0].text.split()[0]
            if name not in infoDict:
                infoDict[name] = float(price)
            with open(file_path, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                count += 1
                #'\r'表示将光标从当前位置移动到行首，所以下一次打印的内容会将上一次的覆盖，从视觉上会觉得实时显示
                print('\r当前速度：{:.2f}%'.format(count*100/len(s_list)), end='')

        except:
            #f.write(str(infoDict) + '\n')
            count += 1
            print('\r当前速度：{:.2f}%'.format(count * 100 / len(s_list)), end='')
            continue
    #print(infoDict)


def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/'
    output_file = './BaiduStockInfo.txt'
    s_list = []
    #demo = getHTMLText(stock_list_url, code='GB2312')
    getStockList(stock_list_url, s_list)
    getStockInfo(stock_info_url, s_list, output_file)

main()