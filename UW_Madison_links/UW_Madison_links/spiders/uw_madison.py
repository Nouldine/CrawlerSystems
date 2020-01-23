
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
from UW_Madison_links.items import UwMadisonLinksItem


class UW_Madison_links( scrapy.Spider ):

    name = 'links_uw'

    #allowed_domains = ['wisc.edu']

    allowed_domains = ['uwm.edu']

    start_urls = [ 

            #"http://guide.wisc.edu/courses/"

            "https://catalog.uwm.edu/courses/"

            ]


    def start_requests( self ):

        for u in self.start_urls:

            yield scrapy.Request( u, callback = self.parse_httpbin,
                    errback = self.errback_httpbin,
                    dont_filter = True )

    def parse_httpbin( self, response ):

        self.logger.info("Go successful respinse {}".format(response.url))

        items = UwMadisonLinksItem()

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



















