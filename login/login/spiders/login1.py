import scrapy
from time import sleep


class Login1Spider(scrapy.Spider):
    name = 'login1'
    allowed_domains = ['wargame.ia.ac.cn/']
    # start_urls = ['http://wargame.ia.ac.cn/login']

    def start_requests(self):
        url = 'https://data.educoder.net/api/accounts/login.json'
        form_data = {
            "login": "1092244357@qq.com",
            "password": "lsb19981220"
        }
        yield scrapy.FormRequest(url, formdata=form_data, callback=self.parse)

    def parse(self, response):
        print(response.text + 'first')
        sleep(3)
        yield scrapy.Request('https://www.educoder.net/problems/on7urxchgi4w/oj/fsc6lvpn', callback=self.parse_info)

    def parse_info(self, response):
        print(response.text)
