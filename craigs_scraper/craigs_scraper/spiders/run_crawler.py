from scrapy.crawler import CrawlerProcess
import scrapy
import sys 
from craig_crawler import Craig_Crawler
from scrapy.utils.project import get_project_settings

if __name__ == "__main__":
    area = sys.argv[1]
    categories = sys.argv[2].split(",")
    process = CrawlerProcess(get_project_settings())
    process.crawl(Craig_Crawler,area,categories)
    process.start()