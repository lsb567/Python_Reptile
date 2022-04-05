from urllib.request import Request, urlopen
from fake_useragent import UserAgent

url = 'https://www.educoder.net/users/mpcsxw4lb/classrooms'
headers = {
    'User-Agent': UserAgent().chrome,
    'Cookie': 'UM_distinctid=17f5870129fae1-09ed374237a3e2-f791b31-144000-17f587012a0e03; autologin_trustie=864429dfad59059978ebb2c3316b13559aa48344; _educoder_session=ba3c3e6007f20049fabcf90b527421fc'
}
request = Request(url, headers=headers)
response = urlopen(request)
print(response.read().decode())