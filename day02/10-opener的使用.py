from urllib.request import Request, build_opener
from fake_useragent import UserAgent
from urllib.request import HTTPHandler
url = 'http://www.baidu.com'
headers = {
    'User-Agent': UserAgent().chrome
}
request = Request(url, headers=headers)
handler = HTTPHandler()
opener = build_opener(handler)
response = opener.open(request)
print(response.read().decode())

