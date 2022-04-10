from jsonpath import jsonpath
from fake_useragent import UserAgent
import requests
import json
url = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"
headers = {
    'User-Agent': UserAgent().chrome
}

response = requests.get(url, headers=headers)
names = jsonpath(json.loads(response.text), '$..name')  # 解析文件需要时json文件， 表达式需要已根目录开头”$”
codes = jsonpath(response.json(), '$..code')

print(names)
print(codes)

for item in zip(names, codes):
    print('城市名称：', item[0], '-----', '城市编号：', item[1])