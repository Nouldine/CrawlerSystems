

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
from plateville_links.items import PlatevilleLinksItem 


class plateville_links(  scrapy.Spider ):

    name = 'plateville_links2'


    allowed_domains = ['uwplatt.edu']

    start_urls = [


  'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/A/GRAD', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/B/GRAD', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/C/GRAD', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/E/GRAD', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/F/GRAD', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/G/GRAD', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/H/GRAD', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/I/GRAD', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/M/GRAD', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/P/GRAD', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/S/GRAD', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/T/GRAD', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/U/GRAD', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/W/GRAD',
  'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/A/XGR', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/B/XGR', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/C/XGR', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/D/XGR', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/E/XGR', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/H/XGR', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/I/XGR', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/M/XGR', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/O/XGR', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/P/XGR',
  'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/A/UGRD', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/B/UGRD', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/C/UGRD', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/E/UGRD', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/F/UGRD', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/G/UGRD', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/H/UGRD', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/I/UGRD', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/J/UGRD', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/L/UGRD', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/M/UGRD', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/N/UGRD', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/P/UGRD', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/R/UGRD', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/S/UGRD', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/T/UGRD', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/U/UGRD', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/W/UGRD',
  'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/A/XUG', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/B/XUG', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/C/XUG', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/E/XUG', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/F/XUG', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/G/XUG', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/H/XUG', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/I/XUG', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/M/XUG', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/P/XUG', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/S/XUG', 'https://passexpress.uwplatt.edu/app/catalog/listSubjectsByLetter/UWPLT/W/XUG'

            ]

    def start_requests( self ): 

        for u in self.start_urls:

             yield scrapy.Request( u, callback = self.parse_httpbin,
                    errback = self.errback_httpbin,
                    dont_filter = True )

    def parse_httpbin( self, response ):

        self.logger.info("Go successful respinse {}".format(response.url))

        items = PlatevilleLinksItem()

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


