from fake_useragent import UserAgent
import requests

session = requests.Session()
headers = {
    'User-Agent': UserAgent().chrome
}
login_url = 'https://data.educoder.net/api/accounts/login.json'
params = {
    'login': '1092244357@qq.com',
    'password': 'lsb19981220'
}
response = session.post(login_url, headers=headers, data=params, verify=False)
info_url = 'https://www.educoder.net/users/mpcsxw4lb/classrooms'
resp = requests.get(info_url, headers=headers)
print(resp.content)
