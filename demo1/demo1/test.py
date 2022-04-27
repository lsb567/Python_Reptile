import requests
from fake_useragent import UserAgent
from lxml import etree

url = 'https://www.maoyan.com/films?catId=2&showType=3'

headers = {
    'User-Agent': UserAgent().chrome
}

response = requests.get(url, headers=headers)
e = etree.HTML(response.text)
names = e.xpath('//div[@class="channel-detail movie-item-title"]/@title')
print(names)