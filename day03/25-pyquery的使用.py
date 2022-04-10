from pyquery import PyQuery as pq
import requests
from fake_useragent import UserAgent

url = "https://www.kuaidaili.com/free/inha/"
headers = {
    'User-Agent': UserAgent().chrome
}
response = requests.get(url, headers=headers)
doc = pq(response.text)
trs = doc('tr')
for num in range(1, len(trs)):
    ip = trs.eq(num).find('td').eq(0).text()
    port = trs.eq(num).find('td').eq(1).text()
    type = trs.eq(num).find('td').eq(3).text()
    print(ip, ":", port, "-----", type)