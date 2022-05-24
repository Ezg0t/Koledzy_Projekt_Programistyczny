# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ZegarkiScraperItem(scrapy.Item):
    producent = scrapy.Field()
    nazwa = scrapy.Field()
    cena = scrapy.Field()
    zdjecie = scrapy.Field()
    link = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
