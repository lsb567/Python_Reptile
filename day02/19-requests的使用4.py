from fake_useragent import UserAgent
import requests

url = 'http://www.12306.cn/mormhweb/'
headers = {
    'User-Agent': UserAgent().chrome
}

response = requests.get(url, verify=False, headers=headers)
response.encoding = 'utf-8'
print(response.text)
