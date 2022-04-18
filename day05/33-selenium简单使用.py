from selenium import webdriver


def chrome_test():
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    chrome.get('http://cn.bing.com')
    chrome.find_element_by_id("sb_form_q").send_keys("python")
    chrome.find_element_by_id("search_icon").click()


def chrome_headless():  # 无头浏览的使用方式
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    chrome = webdriver.Chrome(chrome_options=options)
    chrome.get("http://www.baidu.com")
    html = chrome.page_source
    print(html)


if __name__ == '__main__':
    chrome_headless()