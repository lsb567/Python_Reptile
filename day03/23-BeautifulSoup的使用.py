import requests
from bs4 import BeautifulSoup
from bs4.element import Comment

str = '''
<title id="title">尚学堂</title>
<div class='info' float='left'>Welcome to SXT</div>
<div class='info' float='right'>
    <span>Good Good Study</span>
    <a href='www.bjsxt.cn'></a>
    <strong><!--没用--></strong>
</div>
'''
soup = BeautifulSoup(str, 'lxml')

print(soup.title)
print(soup.div)

print(soup.div.attrs)
print(soup.div['float'])
print(soup.div.get('class'))
print(soup.a['href'])

print(type(soup.div.string))
print(soup.div.text)


if type(soup.strong.string) == Comment:
    print(soup.strong.string)
    print(soup.strong.prettify())  # 注释原样显示
else:
    print(soup.strong.text)

print('------------------find_all------------------')
print(soup.find_all('title'))
print(soup.find_all(id="title"))
print(soup.find_all(class_='info'))
print(soup.find(attrs={'float': 'left'}))
print(soup.find_all('div', attrs={'float': 'left'}))

str2 = '''
<title id="title">尚学堂</title>
<div class='info' float='left'>Welcome to SXT</div>
<div class='info' float='right'>
    <span>Good Good Study</span>
    <a href='www.bjsxt.cn'></a>
    <strong><!--没用--></strong>
</div>
'''

print('------------------css()-------------------')
print(soup.select('title'))
print(soup.select('#title'))  # id选择器
print(soup.select('.info'))  # 类选择器
print(soup.select('div span'))
print(soup.select('div>span'))
print(soup.select('div')[1].select('a'))  # 一层一层的向下筛选即可
print(soup.select('title')[0].string)  # 文本
print(soup.select('title')[0].text)  # 文本