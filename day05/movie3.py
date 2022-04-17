import requests
from fake_useragent import UserAgent
from random import randint
from time import sleep
import re


def get_html(url):
    headers = {
        'User-Agent': UserAgent().chrome
    }
    # sleep(randint(3, 10))
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        return response.text
    else:
        return None


def parse_index(html):
    all_url = re.findall(r'<a href="(/films/\d+)" target="_blank" data-act="movie-click" data-val="{movieid:\d+}">\s+<img', html)
    return ['http://maoyan.com{}'.format(url) for url in all_url]


def parse_info(html):
    name = re.findall(r'<h1 class="name">(.+)</h1>', html)
    types = re.findall(r'<li class="ellipsis">(.+)</li>', html)
    actors = re.findall(r'<li class="celebrity actor".+>\s+<a href="/films/cel.+>\s+<img.+>\s+</a>\s+<div.+>\s+<a.+>\s+(.+)\s+</a>', html)

    # actors = e.xpath('//li[@class="celebrity actor"]//div[@class="info"]/a/text()')
    actors = format_actors(actors)
    return {
        'name': name,
        'types': types,
        'actors': actors
    }


def format_actors(actors):
    actor_set = set()
    for actor in actors:
        actor_set.add(actor)
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