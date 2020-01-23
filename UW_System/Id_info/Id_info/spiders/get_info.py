

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
from Id_info.items import IdInfoItem


class  campus_links( scrapy.Spider ):

    name = "campus_info"
    allowed_domains = ['wisconsin.edu']

    start_urls = [ 

            "https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%2FinstitutionList.do%3FreqType%3DC%26clear%3Dyes"

            ]


    def start_requests( self ):

        for u in self.start_urls:

            yield scrapy.Request( u, callback = self.parse_httpin, 
                    errback = self.errback_httpbin,
                    dont_filter = True )

    def parse_httpin( self, response ):

        self.logger.info("Got successful response {}".format(response.url) )
        
        
        fromInstitutionId = response.xpath('//select[@name="fromInstitutionId"]/option/@value').extract() 
        institutionName = response.xpath('//select[@name="fromInstitutionId"]/option/text()').extract()

        from_institution_final  = []
        institution_name = []

        item = [] 
        track_index = 0
        vec_size = len(fromInstitutionId)

        while track_index < vec_size:

            items = IdInfoItem()
            
            items['fromInstitutionId'] = fromInstitutionId[ track_index ]
            items['institutionName'] = institutionName[ track_index ]

            item.append(items)

            track_index += 1

        return  item


    def  errback_httpbin( self, failure ):

        # log all failures
        self.logger.error(repr(failure))

        # in case you wann to do somethingn special for some errors. 
        # you may need the failure's type

        if failure.check(HttpError):

            # These exception com from HttpError spider middleware 
            # you can gert the non-200 response
            response = failure.value.response
            self.logger.error("HttpError on %s",  response.url )

        elif failure.check(DNSLookupError):

            # This is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url )
        
        elif failure.check(TimeoutError, TCPTimeOutError ):

             request = failure.request
             self.logger.error('TimeoutError on %s', request.url )




















