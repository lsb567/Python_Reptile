import re

import requests
from fake_useragent import UserAgent

url = 'http://www.921131.com/'
headers = {
    'User-Agent': UserAgent().chrome
}
# 构造请求
response = requests.get(url, headers=headers)
info = response.text
# print(info)
infos = re.findall(r'<div class="post-body">\s*<p>\s*(.+)\s*<p style="text-align: center;">', info)
print(infos)
with open('duanzi.txt', 'w', encoding='utf-8') as f:
    for info in infos:
        f.write(info + "\n\n\n")