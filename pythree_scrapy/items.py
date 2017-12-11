# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class PythreeScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class iFengNewItem(scrapy.Item):
    # http://gz.house.ifeng.com/ item
    title = Field()
    time = Field()
    content = Field()
    news_from = Field()
    news_type = Field()
    # viewNum = Field()       # 点击量
    # plNum = Field()         # 评论数
    pass