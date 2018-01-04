import requests
import pandas as pd
from bs4 import BeautifulSoup

def getHTML(url):
    r = requests.get(url)
    try:
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


def getInfo(html):

    soup = BeautifulSoup(html, 'html.parser')
    ol = soup.find('ol',class_ ="grid_view")
    li = ol.find_all('li')
    for l in li:
        try:
            span = l.find('span', class_="title")
            title = span.get_text()
            title_list.append(title)
            p = l.find('p', class_="")
            director = p.get_text().split()[1]
            director_list.append(director)
            spa = l.find('span', class_ = "inq")
            if spa is None:
                quote = '########'
            else:
                quote = spa.get_text()
            introduce_list.append(quote)
            a = l.find('a')
            if a is None:
                link = '########'
            else:
                link = a['href']
            link_list.append(link)

        except:
            continue


if __name__ == '__main__':
    url = 'https://movie.douban.com/top250?start='
    count = 10
    movie_info = {}
    title_list = []
    director_list = []
    introduce_list = []
    link_list = []
    for i in range(count):
        html_url = url + str(25*i)
        html = getHTML(html_url)
        getInfo(html)
    movie_info['title'] = title_list
    movie_info['director'] = director_list
    movie_info['quote'] = introduce_list
    movie_info['link'] = link_list
    info = pd.DataFrame(movie_info)
    info = info[['title', 'director', 'quote', 'link']]
    info.to_csv('./Top250.csv', mode='w', encoding='utf_8_sig')
