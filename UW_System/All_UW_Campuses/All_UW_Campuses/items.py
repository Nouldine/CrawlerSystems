# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import  Item, Field

class AllUwCampusesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    course_1    = scrapy.Field()
    title_1     = scrapy.Field()
    course_2    = scrapy.Field()
    title_2     = scrapy.Field()
    credits     = scrapy.Field()
    gen_ed      = scrapy.Field()
    level       = scrapy.Field()
    special     = scrapy.Field()
    from_       = scrapy.Field()
    to          = scrapy.Field()

    pass
