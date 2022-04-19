import requests
from fake_useragent import UserAgent
from lxml import etree

url = "https://redtea1001.tuchong.com/101965431/"
response = requests.get(url, headers={"User-Agent": UserAgent().chrome})
e = etree.HTML(response.text)
img_urls = e.xpath('//article/img/@src')

print(img_urls)
for url in img_urls:
    response = requests.get(url, headers={"User-Agent": UserAgent().chrome})
    img_name = url[url.rfind('/') + 1:]  # rfind()：会返回找到的最后一个索引的下标
    with open('img/' + img_name, 'wb') as f:
        f.write(response.content)