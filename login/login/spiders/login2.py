import scrapy


class Login2Spider(scrapy.Spider):
    name = 'login2'
    allowed_domains = ['kyfw.12306.cn']
    # start_urls = ['http://wargame.ia.ac.cn/usercenter/info/user/edit']

    def start_requests(self):
        cookie_str = '_passport_session=0e5dc634d35a4fa485ee86d7b1300b843036; BIGipServerportal=3084124426.17183.0000; BIGipServerotn=3705078026.64545.0000; BIGipServerpassport=887619850.50215.0000; RAIL_EXPIRATION=1651843167166; RAIL_DEVICEID=gZZVa6FdUwElxiS5arQ-tvKIJP5w3LQCXLnN9j41TA1bceOVCDTf6ggBt-KSfhlE2xYUymgZ93b5Sb9UjLacjYIaCDJ-YDnQ2b79VuvP-J66ZVqbocxgWRD33qrZyrxCF34Q7pXH2EC3Bf70bgne5e-4s2t-rf4i; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; route=495c805987d0f5c8c84b14f60212447d'
        cookies = {}
        for cookie in cookie_str.split(';'):
            key, value = cookie.split('=', 1)
            cookies[key.strip()] = value.strip()
        yield scrapy.Request('https://kyfw.12306.cn/otn/view/index.html', cookies=cookies, callback=self.parse)

    def parse(self, response):
        print(response.text)
