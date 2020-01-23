
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
from uw_Green_Bay.items import UwGreenBayItem 


class uw_green_bay( CrawlSpider ):

    name = 'green_bay'
    allowed_domains = ['uwgb.edu']

    
    start_urls = [ 

            "http://catalog.uwgb.edu/undergraduate/programs/"

            ]

     rules = (

            Rule( LinkExtractor( allow = ( r'http://catalog.uwgb.edu/undergraduate/programs/' )),

                callback = 'parse_httpbin',

                follow = True

                ),

            )

    def parse_httpbin( self, response ):

        items =  UwGreenBayItem()

        course  = response.css('div.blockindent > a.bubblelink.code::text').extract()
        title =  response.css('#wrapper > #container > #content-col > #content > #textcontainer > table > tbody > tr.odd > td::text').extract() 
        #response.css('#wrapper > #container > #content-col > #content > #textcontainer > table > tbody > tr > td::text').extract()
        description = response.css('.courseblockdesc').extract() 
     





















