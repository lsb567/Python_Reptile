import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Zww2Spider(CrawlSpider):
    name = 'zww2'
    allowed_domains = ['86zw.co']
    start_urls = ['http://www.86zw.co/xiaoshuo/3315/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=r'//div[@id="list"]/dl/dd[10]/a'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths=r'//div[@class="bottem1"]/a[4]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        title = response.xpath('//h1/text()').extract_first()
        content = ''.join(response.xpath('//div[@id="content"]/text()').extract()).replace('    ', '    ')

        yield {
            'title': title,
            'content': content
        }
