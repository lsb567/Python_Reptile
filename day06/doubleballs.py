import requests
from fake_useragent import UserAgent
from lxml import etree

url = "https://datachart.500.com/ssq/"

response = requests.get(url, headers={'UserAgent': UserAgent().chrome})
e = etree.HTML(response.text)
data_times = e.xpath('//tbody[@id="tdata"]/tr/td[1]/text()')
trs = e.xpath('//tbody[@id="tdata"]/tr[not(@class)]')

for data_time, tr in zip(data_times, trs):

    red_ball = '-'.join(tr.xpath('./td[@class="chartBall01"]/text()'))
    blue_ball = tr.xpath('./td[@class="chartBall02"]/text()')[0]
    print('第 ' + data_time + '期： 红球是：' + red_ball + '蓝球：' + blue_ball)