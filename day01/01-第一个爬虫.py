from urllib.request import urlopen

url = "http://www.baidu.com"
# 发送请求
response = urlopen(url)
# 读取内容
info = response.read()
# 打印内容
print(info.decode())


# # 打印状态码
# print(response.getcode())
# # 打印真实url
# print('---------------')
# print(response.geturl())
# # 打印响应头
# print('-------------')
# print(response.info())
