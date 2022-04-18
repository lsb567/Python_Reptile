from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
url = 'https://www.huya.com/g/lol'
driver.get(url)
num = 1
while True:
    print('第' + str(num) + '页------------------------------------------------')
    num += 1
    sleep(2)  # 运行速度过快，可能页面代码还没有加载出来，导致爬取出错
    html = driver.page_source
    names = driver.find_elements_by_xpath('//i[@class="nick"]')
    counts = driver.find_elements_by_xpath('//i[@class="js-num"]')
    for name, count in zip(names, counts):
        print(name.text, ":", count.text)
    if driver.page_source.find('laypage_next') != -1:
        driver.find_element_by_xpath('//a[@class="laypage_next"]').click()
    else:
        break

