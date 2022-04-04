from urllib.request import urlopen

url = "http://www.baidu.com"
# 发送请求
respone = urlopen(url)
# 读取内容
info = respone.read()
# 打印内容
print(info)
