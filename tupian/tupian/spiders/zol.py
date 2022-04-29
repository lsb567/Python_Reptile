import scrapy


class ZolSpider(scrapy.Spider):
    name = 'zol'
    allowed_domains = ['zol.com.cn']
    start_urls = ['https://desk.zol.com.cn/bizhi/9906_119049_2.html']

    def parse(self, response):
        image_url = response.xpath('//img[@id="bigImg"]/@src').extract()
        image_name = response.xpath('string(//h3)').extract_first()
        yield {
            "image_urls": image_url,
            "image_name": image_name
        }
        next_url = response.xpath('//a[@id="pageNext"]/@href').extract_first()
        if next_url.find('.html') != -1:
            yield scrapy.Request(response.urljoin(next_url), callback=self.parse)
