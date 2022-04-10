from lxml import etree
import requests
from fake_useragent import UserAgent

url = "https://m.qidian.com/book/1021617576.html"
headers = {
    'User-Agent': UserAgent().chrome
}

response = requests.get(url, headers=headers)
e = etree.HTML(response.text)
names = e.xpath('//h2/text()')
author = e.xpath('//div[@class="book-rand-a"]/a/text()[1]')

print(names)
print(author)