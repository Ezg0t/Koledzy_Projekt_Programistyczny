import sys
import pymongo

sys.path.insert(0, 'C:\\Users\\krylo\\Desktop\studia\\projekt_koledzy\\venv\\zegarki_scraper\\zegarki_scraper')
from items import ZegarkiScraperItem
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
class MongoDBPipeline:
    collection = 'scrapy_items'

    def __init__(self, mongodb_uri, mongodb_db):
        self.mongodb_uri = 'mongodb+srv://koledzy_projekt:u1mkLXkE4niiONPd@cluster0.hwii5.mongodb.net/test'
        self.mongodb_db = 'zegarki'
        if not self.mongodb_uri: sys.exit("You need to provide a Connection String.")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongodb_uri=crawler.settings.get('MONGODB_URI'),
            mongodb_db=crawler.settings.get('MONGODB_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongodb_uri)
        self.db = self.client[self.mongodb_db]
        # Start with a clean database
        self.db[self.collection].delete_many({})

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = dict(ZegarkiScraperItem(item))
        self.db[self.collection].insert_one(data)
        return item