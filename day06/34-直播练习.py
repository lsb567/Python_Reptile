from selenium import webdriver


driver = webdriver.Chrome()
url = 'https://www.huya.com/g/lol'
driver.get(url)
html = driver.page_source
names = driver.find_element_by_xpath('//i[@class="nick"]')
counts = driver.find_element_by_xpath('//i[@class="js-num"]')
for name, count in zip(names, counts):
    print(name, ":", count)
print(html)
