import requests
from fake_useragent import UserAgent
from random import randint
from time import sleep
from pyquery import PyQuery as pq


def get_html(url):
    headers = {
        'User-Agent': UserAgent().chrome
    }
    sleep(randint(2, 5))
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        return response.text
    else:
        return None


def parse_index(html):
    doc = pq(html)
    all_a = doc('.channel-detail.movie-item-title a')
    all_url = []
    for a in all_a:
        all_url.append(a.attrib['href'])
    # e = etree.HTML(html)
    # all_url = e.xpath('//div[@class="channel-detail movie-item-title"]/a/@href')
    # # print(all_url, '1')
    return ['http://maoyan.com{}'.format(url) for url in all_url]


def parse_info(html):
    doc = pq(html)
    name = doc('h1.name')  # 同样，动态网页获取不到，乌鱼子
    types = doc('li.ellipsis')
    actors = doc('li.celebrity actor > div.info > a')


    # e = etree.HTML(html)
    # name = e.xpath('//h1[@class="name"]/text()')
    # types = e.xpath('//li[@class="ellipsis"]/a/text()')
    # actors = e.xpath('//li[@class="celebrity actor"]//div[@class="info"]/a/text()')
    actors = format_actors(actors)
    return {
        'name': name,
        'types': types,
        'actors': actors
    }


def format_actors(actors_a):
    actor_set = set()
    for a in actors_a:
        actor_set.add(a.text.strip())
    return actor_set


def main():
    index_url = 'http://maoyan.com/films'
    html = get_html(index_url)
    movie_urls = parse_index(html)
    print('----')
    print(movie_urls, 'movie_urls')
    for url in movie_urls:
        movie_html = get_html(url)
        movie = parse_info(movie_html)
        print(movie, 'movie')  # 网站现在变成动态了，所以获取不到了，乌鱼子


if __name__ == '__main__':
    main()