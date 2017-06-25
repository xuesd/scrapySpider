# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ScrapyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Xicidaili(scrapy.Item):
    ip = scrapy.Field()
    port = scrapy.Field()
    position = scrapy.Field()
    anonymous = scrapy.Field()
    type = scrapy.Field()
    speed = scrapy.Field()
    connect_time = scrapy.Field()
    last_check_time = scrapy.Field()