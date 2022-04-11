from threading import Thread
from queue import Queue
from fake_useragent import UserAgent
import requests
from lxml import etree


# 爬虫类
class CrawlInfo(Thread):
    def __init__(self, url_queue, html_queue):
        Thread.__init__(self)
        self.url_queue = url_queue
        self.html_queue = html_queue

    def run(self):
        headers = {
            'User-Agent': UserAgent().chrome
        }
        while not self.url_queue.empty():
            response = requests.get(self.url_queue.get(), headers=headers)

            print(response.text)
            if response.status_code == 200:
                self.html_queue.put(response.text)
                # print(html_queue.empty())
                # print(response.text)
                # print(self.html_queue)


# 解析类
class ParseInfo(Thread):
    def __init__(self, html_queue):
        Thread.__init__(self)
        self.html_queue = html_queue
        # print(html_queue)

    def run(self):
        # print(self.html_queue.empty())
        while not self.html_queue.empty():
            e = etree.HTML(self.html_queue.get())
            # print(e)
            contents = e.xpath('///div[@class="c_de_rk_c_data margin"]/a')
            with open('duanzi.txt', 'a', encoding='utf-8') as f:
                for item in contents:
                    info = item.xpath('string(.)')
                    f.write(info + '\n')


if __name__ == '__main__':
    # 存储url的容器
    url_queue = Queue()
    # 存储内容的容器
    html_queue = Queue()
    base_url = 'https://b.faloo.com/Rank_{}.html/'
    for i in range(2, 3):
        new_url = base_url.format(i)
        url_queue.put(new_url)
    # 创建一个爬虫
    crawl_list = []
    for i in range(0, 3):
        crawl1 = CrawlInfo(url_queue, html_queue)
        crawl_list.append(crawl1)
        crawl1.start()
    for crawl in crawl_list:
        crawl.join()
    # print(html_queue.empty())
    parse_list = []
    for i in range(0, 3):
        parse = ParseInfo(html_queue)
        parse_list.append(parse)
        parse.start()
    for parse in parse_list:
        parse.join()