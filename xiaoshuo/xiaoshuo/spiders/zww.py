import scrapy


class ZwwSpider(scrapy.Spider):
    name = 'zww'
    allowed_domains = ['86zw.co']
    start_urls = ['http://www.86zw.co/xiaoshuo/3334/88052178.html']

    def parse(self, response):
        title = response.xpath('//h1/text()').extract_first()
        content = ''.join(response.xpath('//div[@id="content"]/text()').extract()).replace('    ', '    ')

        yield {
            'title': title,
            'content': content
        }
        next_url = response.xpath('//div[@class="bottem2"]/a[4]/@href').extract_first()
        # base_url = 'http://www.86zw.co{}'.format(next_url)
        if next_url.find('.html') != -1:
            yield scrapy.Request(response.urljoin(next_url), callback=self.parse)

