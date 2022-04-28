import scrapy


class ZwwSpider(scrapy.Spider):
    name = 'zww'
    allowed_domains = ['86zw.co']
    start_urls = ['http://86zw.co/']

    def parse(self, response):
        pass
