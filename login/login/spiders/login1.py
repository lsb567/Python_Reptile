import scrapy
from time import sleep


class Login1Spider(scrapy.Spider):
    name = 'login1'
    allowed_domains = ['kyfw.12306.cn']
    # start_urls = ['http://wargame.ia.ac.cn/login']

    def start_requests(self):
        url = 'https://kyfw.12306.cn/passport/web/checkLoginVerify'
        form_data = {
            "username": "17362353715",
            "appid": "otn"
        }
        yield scrapy.FormRequest(url, formdata=form_data, callback=self.parse)

    def parse(self, response):
        print(response.text + 'first')
        sleep(3)
        yield scrapy.Request('https://kyfw.12306.cn/otn/view/index.html', callback=self.parse_info)

    def parse_info(self, response):
        print(response.text + 'second')
