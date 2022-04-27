# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class Demo1Pipeline:
    def open_spider(self, spider):
        self.filename = open('movie.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        if item['type'] == '喜剧':
            pass
        # with open('movie.txt', 'a', encoding='utf-8') as f:
        #     f.write(json.dumps(item, ensure_ascii=False) + '\n')
        # print(item)
        self.filename.write(json.dumps(dict(item), ensure_ascii=False) + '\n')
        return item

    def close_spider(self, spider):
        self.filename.close()
