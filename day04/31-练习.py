import requests
from fake_useragent import UserAgent
from lxml import etree
url = 'http://www.farmer.com.cn/2022/03/28/99891372.html'

headers = {
    'User-Agent': UserAgent().chrome
}

response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
# print(response.text)
e = etree.HTML(response.text)
title = e.xpath('//h1/text()')
all_p_tag = e.xpath('//div[@class="article-main"]//p')
content = []
for p in all_p_tag:
    info = p.xpath('string(.)')
    content.append(info)
content_str = ''.join(content)
img_urls = e.xpath('//div[@class="article-main"]//img/@src')
img_names = e.xpath('//div[@class="article-main"]//span/text()')
for i in range(len(img_names)):
    img_name = img_names[i]

