# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SaleItem(scrapy.Item):
    url = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()
    category = scrapy.Field()