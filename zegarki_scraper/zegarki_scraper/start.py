from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
class odpal():
    def scrapy_to_db():
        process = CrawlerProcess(get_project_settings())
        process.crawl('zegarownia')
        process.start()
odpal.scrapy_to_db()