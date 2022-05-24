import scrapy

import sys
sys.path.insert(0, 'C:\\Users\\krylo\\Desktop\studia\\projekt_koledzy\\venv\\zegarki_scraper\\zegarki_scraper')
from items import ZegarkiScraperItem



class ZegarowniaSpider(scrapy.Spider):
    name = "zegarownia"
    start_urls = [
        'https://zegarownia.pl/zegarki-meskie/mechanizm:smartwatch'
    ]

    def parse(self, response):
        for products in response.css('div.product-item-info'):
            item={}
            item = ZegarkiScraperItem()
            jakaCena=0
            producent=products.css('span.product-item-link__manufacturer::text').get().replace('\n', '').strip()
            nazwa=products.css('span.product-item-link__name::text').get().replace('\n', '').strip()
            if products.css('span.price-container.price-final_price.tax.weee::text').get() != None:
                jakaCena = products.css('span.price-container.price-final_price.tax.weee::text').get()
                jakaCena = jakaCena.replace('\xa0', '')
                jakaCena = jakaCena.replace('\n', '').strip()
            else:
                jakaCena = products.css('span.special-price::text').get()
                jakaCena =jakaCena.replace('\xa0','')
            jakaCena=jakaCena.replace('zł','')
            #if products.css('product-image-photo.lazyload.first').get()!=None:
            if products.css('img.product-image-photo.lazyload.first').get() is not None:
                zdjecie = products.css('img.product-image-photo.lazyload.first').attrib['data-src']
            elif products.css('img.product-image-photo.first').attrib['onerror'] is not None:
                zdjecie=products.css('img.product-image-photo.first').attrib['onerror'].replace('this.onerror=null; this.src=','')
                zdjecie=zdjecie[1:-1]
            else:
                zdjecie='brak'

            item['producent'] = producent
            item['nazwa'] = nazwa
            item['cena'] = jakaCena
            item['zdjecie'] = zdjecie
            item['link'] = products.css('a.product-item-link').attrib['href']
            yield item
            '''
            yield {
                'producent': producent,
                'nazwa':nazwa,
                'cena':jakaCena,
                'zdjecie':zdjecie,
                #'zdjecie': products.css('img.product-image-photo.first').attrib['src'],
                'link':products.css('a.product-item-link').attrib['href'],
            }
'''
            #products.css('span.product-item-link__manufacturer::text').get() - nazwa firmy
            #products.css('span.product-item-link__name::text').get() - model
            #products.css('span.price-container.price-final_price.tax.weee::text').get() - cena bez przecen
            #products.css('span.old-price::text').get()  - stara cena
            #products.css('span.special-price::text').get()
            #products.css('a.product-item-link').attrib['title']
            #products.css('a.product-item-link').attrib['href']
        next_page = response.css('a.action.primary.arrowed.next').attrib['href']

        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)
        next_page = response.css('a.action.next').attrib['href']

        # scrapy crawl zegarownia -O smartwatche.json

        #action primary arrowed next
        #response.css('a.action.primary.arrowed.next').get()
        #response.css('a.action.primary.arrowed.next').attrib['href']





