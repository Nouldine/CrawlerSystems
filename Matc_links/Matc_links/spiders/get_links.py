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
from Matc_links.items import MatcLinksItem

class Matc_links(  scrapy.Spider ):

    name = 'matc_links'

    allowed_domains = ['madisoncollege.edu']

    start_urls = [

            'https://my.madisoncollege.edu/app/catalog/listCatalog/MATC1/DEGR',
            'https://my.madisoncollege.edu/app/catalog/listCatalog/MATC1/NDEG'

            ]


    def start_requests( self ):

        for u in self.start_urls:

            yield scrapy.Request( u, callback = self.parse_httpbin,
                    errback = self.errback_httpbin,
                    dont_filter = True )

    def parse_httpbin( self, response ):

        self.logger.info("Go successful respinse {}".format(response.url))

        items = MatcLinksItem()

        links = response.xpath('*//a/@href').extract()

        items['links'] = links

        yield items


    def errback_httpbin( self,  failure):

        # log all failures
        self.logger.error(repr(failure))

        # in case you want to do something special for some errors,
        # you may need the non-200 response
        if failure.check(HttpError):

            # These exception come from HttpError spider middleware
            # you can get non-200 response
            response = failure.value.response
            self.logger.error("HttpError on %s", response.url )

        elif failure.check(DNSLookupError):

            # This is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %', request.url)

        elif failure.check( TimeoutError, TPCTimeOutError ):

            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)

        






















