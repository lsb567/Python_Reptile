import requests
from fake_useragent import UserAgent

headers = {
    'User-Agent': UserAgent().chrome
}
login_url = 'https://data.educoder.net/api/accounts/login.json'
params = {
    'login': '1092244357@qq.com',
    'password': 'lsb19981220'
}

response = requests.post(login_url, headers=headers, data=params)
print(response.text)
