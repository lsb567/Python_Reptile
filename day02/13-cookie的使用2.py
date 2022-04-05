from urllib.request import Request, urlopen
from fake_useragent import UserAgent
from urllib.parse import urlencode
from urllib.request import HTTPCookieProcessor, build_opener
# 登录
login_url = "https://data.educoder.net/api/accounts/login.json"
headers = {
    'User-Agent': UserAgent().chrome,
}
form_data = {
    'login': '1092244357@qq.com',
    'password': 'lsb19981220'
}
f_data = urlencode(form_data).encode()
request = Request(login_url, headers=headers, data=f_data)
# response = urlopen(request) 错误的
handler = HTTPCookieProcessor()
opener = build_opener(handler)
response = opener.open(request)
print(response.read().decode())
# 访问页面
info_url = 'https://www.educoder.net/users/mpcsxw4lb/classrooms'
request = Request(info_url, headers=headers)
# response = urlopen(request)
response = opener.open(request)
print(response.read().decode())
