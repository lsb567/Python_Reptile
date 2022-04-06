import requests
from fake_useragent import UserAgent

headers = {
    'User-Agent': UserAgent().chrome
}
url = 'https://www.baidu.com'
params = {
    'wd': '尚学堂'
}

response = requests.get(url, headers=headers, params=params)
print(response.text)
