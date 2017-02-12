# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class JsonPipeline(object):

    def process_item(self, item, spider):
        spider.visited.append(item)

    def close_spider(self,spider):
        with open('visited.json','r') as f:
            temp =[]
            for line in f:
                temp.append(json.loads(line))
            output = open('output.json','w')
            for x in spider.visited:
                if x['url'] not in temp:
                    line = json.dumps(dict(x)) + "\n"
                    output.write(line)
        with open('visited.json','w') as f:
            for x in spider.visited:
                line = json.dumps(x['url']) + "\n"
                f.write(line)






                
