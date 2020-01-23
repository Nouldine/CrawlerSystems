
from scrapy import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.linkextractors import LinkExtractor
import scrapy
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError
from w3lib.html import remove_tags
from UW_oshkosh.items import UwOshkoshItem


class Oshkosh_courses( CrawlSpider ):

    name =  'uw_oshkosh_courses'

    allowed_domains = ['uwosh.edu']

    start_urls = [

            "https://www.uwosh.edu/registrar/undergradbulletins/2017-2019/departments-and-majors/african-american-studies-1" 
            ]


    rules = (

            Rule( LinkExtractor( allow = (r'https://www.uwosh.edu/registrar/undergradbulletins/2017-2019/departments-and-majors/')), 

                callback = 'parse_httpbin',

                follow = True 


            ),
    )

    def parse_httpbin( self, response ):

        items = UwOshkoshItem() 

        course = response.xpath('//tr/td[@width="375"]/p').extract()
        unit = response.xpath('//tr/td[@width="332"]/p').extract()
        description = response.xpath('///tr/td[1][@width="707"]/p[1][1]/text()').extract()

  
        items['course'] = course
        items['unit'] = unit
        items['description'] = description


        yield items






















