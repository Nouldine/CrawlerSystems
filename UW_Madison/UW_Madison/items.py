# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
#from scrapy.loader.processors import Join, MapCompose, TakeFirst
#from w3lib.html import remove_tags
from scrapy.item import Item, Field


class UwMadisonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    course = scrapy.Field()
    title = scrapy.Field()
    unit = scrapy.Field()
    description = scrapy.Field()
    prerequisites = scrapy.Field()

    pass
