import requests
from fake_useragent import UserAgent
from lxml import etree
url = 'http://www.farmer.com.cn/2022/03/28/99891372.html'

headers = {
    'User-Agent': UserAgent().chrome
}

response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
print(response.text)
# e = etree.HTML(response.text)
# title = e.xpath('')
# context = e.xpath('')
# img_urls = e.xpath('')


