from urllib.request import Request, urlopen
from fake_useragent import UserAgent
from urllib.error import URLError
url = 'https://www.sxt.cn/index/login/login'

headers = {
    'User-Agent': UserAgent().chrome
}
try:
    request = Request(url, headers=headers)
    response = urlopen(request)
    print(response.read().decode())
except URLError as e:
    if e.args is None:
        print(e.code)
    else:
        print(e.args[0].errno)
    print(e)
print('访问完成')
