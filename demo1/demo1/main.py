from scrapy.cmdline import execute

execute('scrapy crawl baidu'.split())  # baidu是名字

execute(['scrapy', 'crawl', 'baidu'])  # 第二种写法