import re

str1 = 'I Study Python3.6 Everyday'
print('-----------match()----------')
m1 = re.match(r'I', str1)
m2 = re.match(r'\w', str1)  # 匹配数字字母下划线
m3 = re.match(r'.', str1)
m4 = re.match(r'\D', str1)  # 匹配任意非数字
m5 = re.match(r'i', str1, re.I)  # 不区分大小写
m6 = re.match(r'\S', str1)  # 匹配任意非空字符
m7 = re.match(r'Study', str1)  # 匹配不到，因为match是从左开始匹配
print(m1.group(), m2.group(), m3.group(), m4.group(), m5.group(), m6.group())

print('------------search()-------------')
s1 = re.search(r'Study', str1)
s2 = re.search(r'S\w+', str1)
s3 = re.search(r'P\w+.\d', str1)
print(s1.group(), s2.group(), s3.group())

print('-------------findall()--------------')
f1 = re.findall(r'y', str1)
print(f1)

print('----------------test()------------------')
str2 = '<div><a herf="http://www.bjsxt.com">尚学堂bjsxt</a></div>'
t1 = re.findall(r'[\u4e00-\u9fa5]\w+', str2)  # [\u4e00-\u9fa5]:匹配中文
t2 = re.findall(r'<a herf="http://www.bjsxt.com">(.+)</a>', str2)
t3 = re.findall(r'<a herf="(.+)">', str2)
print(t1, t2, t3)

print('-----------------sub()-------------------')
su1 = re.sub(r'<div>(.+)</div>', r'<span>\1</sp>', str2)  # \1: 分组，第一组放在这里
print(su1)
