from selenium import webdriver
from lxml import etree
from time import sleep

url = 'https://search.jd.com/search?keyword=mac&qrst=1&wq=mac&stock=1&ev=exbrand_Apple%5E'

chrome = webdriver.Chrome()
chrome.get(url)

# js代码拉动滚动条
js = 'document.documentElement.scrollTop=10000'
chrome.execute_script(js)
sleep(3)  # 等待加载

html = chrome.page_source
e = etree.HTML(html)
prices = e.xpath('//div[@class="gl-i-wrap"]/div[@class="p-price"]/strong/i/text()')
names = e.xpath('//div[@class="gl-i-wrap"]/div[@class="p-name p-name-type-2"]/a/em')


print(len(names))
for name, price in zip(names, prices):
    print(name.xpath('string(.)'), ':', price)
