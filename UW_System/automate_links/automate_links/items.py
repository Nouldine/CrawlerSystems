# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class AutomateLinksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    from_campus_id      = scrapy.Field() 
    to_campus_id        = scrapy.Field()
    department_name     = scrapy.Field()
    department_id       = scrapy.Field()

    pass
