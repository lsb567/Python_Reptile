import scrapy
from demo1.items import MovieItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://www.maoyan.com/films?catId=2&showType=3']

    def parse(self, response):
        names = response.xpath('//div[@class="channel-detail movie-item-title"]/@title').extract()
        scores_div = [score.xpath('string(.)').extract_first() for score in response.xpath('//div[@class="channel-detail channel-detail-orange"]')]
        # scores = []
        # for score in scores_div:
        #     scores.append(score.xpath('string(.)').extract_first())

        # for name, score in zip(names, scores_div):
        #     # print(name, ':', score)
        #     yield {'name': name, 'score': score}

        item = MovieItem()
        for name, score in zip(names, scores_div):
            item['name'] = name
            item['score'] = score

            if response.url.find('catId=2') != -1:
                item['type'] = '喜剧'
            elif response.url.find('catId=3') != -1:
                item['type'] = '爱情'
            yield item
