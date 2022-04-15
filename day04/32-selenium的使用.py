from selenium import webdriver


chrome = webdriver.Chrome()

chrome.get('http://www.baidu.com')
# chrome.save_screenshot('baidu.png')  # 截图
html = chrome.page_source
print(html)