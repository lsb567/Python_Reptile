from fake_useragent import UserAgent
import requests

url = 'http://httpbin.org/get'
headers = {
    'User-Agent': UserAgent().chrome
}
proxies = {
    'http': 'http://152.136.62.181:9999'
}
response = requests.get(url, headers=headers, proxies=proxies)
print(response.text)
