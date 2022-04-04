from urllib.request import Request, urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent
import random
args = {
    "wd": "尚学堂",
    "ie": "utf-8"
}
print(urlencode(args))
url = "https://www.baidu.com/s?{}".format(urlencode(args))
print(url)
headers = {
    "User-Agent": UserAgent().random
}
requests = Request(url, headers=headers)
response = urlopen(requests)
info = response.read()
print(info.decode())

