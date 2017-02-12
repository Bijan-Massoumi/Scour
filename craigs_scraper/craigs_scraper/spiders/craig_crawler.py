import scrapy
from scrapy.crawler import CrawlerProcess
import json
from items import SaleItem
import sys 

class Craig_Crawler(scrapy.Spider):
    name = "craig"
    allowed_domains = ["craigslist.org"]
    COOKIES_ENABLED = False
    urls = []
    keyTerms = []
    FEED_FORMAT = "jsonlines"


    def __init__(self, area,categories):
        self.area = area
        if len(categories) > 1:
            self.urls.append("https://%s.craigslist.org/search/%s" % (area,categories[0]))
            self.urls.append("https://%s.craigslist.org/search/%s" % (area,categories[1]))
        else:
            self.urls.append("https://%s.craigslist.org/search/%s" % (area,categories[0]))
        self.visited = []

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse) 

    def parse(self,response):
        saleItems = response.selector.xpath('//li[contains(@class, "result-row")]')
        for item in saleItems:
            sale = SaleItem()
            sale['description'] = item.xpath(".//a[contains(@class,'result-title hdrlnk')]/text()").extract()[0]
            url2 = item.xpath(".//a[contains(@class,'result-title hdrlnk')]/@href").extract()[0]
            sale['url'] = "https://%s.craigslist.org%s" % (self.area,url2) 
            price = item.xpath(".//span[contains(@class,'result-price')]/text()")
            if price != []:
                sale['price'] = price.extract()[0]
            else:
                sale['price'] = "Free"
            sale['category'] = response.url.split('/')[-1]
            yield sale






