from urllib.request import Request, build_opener, HTTPCookieProcessor
from fake_useragent import UserAgent
from http.cookiejar import MozillaCookieJar
from urllib.parse import urlencode


# 登录
# 保存cookie到文件中
def get_cookie():
    login_url = 'https://data.educoder.net/api/accounts/login.json'
    headers = {
        'User-Agent': UserAgent().chrome
    }
    form_data = {
        'login': '1092244357@qq.com',
        'password': 'lsb19981220'
    }
    f_data = urlencode(form_data).encode()
    request = Request(login_url, headers=headers, data=f_data)
    cookie_jar = MozillaCookieJar()
    handler = HTTPCookieProcessor(cookie_jar)
    opener = build_opener(handler)
    response = opener.open(request)
    cookie_jar.save('cookie.txt', ignore_expires=True, ignore_discard=True)


def use_cookie():
    info_url = 'https://www.educoder.net/users/mpcsxw4lb/classrooms'
    headers = {
        'User-Agent': UserAgent().chrome
    }
    request = Request(info_url, headers=headers)
    cookie_jar = MozillaCookieJar()
    cookie_jar.load('cookie.txt', ignore_expires=True, ignore_discard=True)
    handler = HTTPCookieProcessor(cookie_jar)
    opener = build_opener(handler)
    response = opener.open(request)
    print(response.read().decode())


# 获取cookie从文件中
# 访问页面
if __name__ == '__main__':
    # get_cookie()
    use_cookie()
