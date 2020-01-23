

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
from uw_system.items import UwSystemItem 



class uw_system( scrapy.Spider ): 

    name = 'uw_system'
    allowed_domains = ['wisconsin.edu']

    start_urls = [
            
            "https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D310EE116C932F326F4DB0D473D13D51B&tispage=2&fromField=nothingChanged&fromInstitutionId=4684&reqType=C&toInstitutionId=4690&departmentId=0701&submitButton=Match+All+Courses"

            ]
   
    
    def  start_requests( self ):

        for u in self.start_urls:

            yield scrapy.Request( u, callback = self.parse_httpbin,
                    errback = self.errback_httpbin,
                    dont_filter = True )


    def parse_httpbin( self, response ):

        self.logger.info("Got successful response {}".format(response.url) )

        items = UwSystemItem() 
            
        course = response.css('.campus-one-list::text').extract();
        course = response.xpath('#reportTable').extract() 
        items['course'] = course
        
        yield items
            
            
    def errback_httpbin( self, failure):

        # log all failures
        self.logger.error(repr(failure))

        # in case you want to do something special for some errors,
        # you may need the failure's type:

        if failure.check(HttpError):

            # These exception come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error("HttpError on %s", response.url )

        elif failure.check(DNSLookupError):

            # This is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url )

        elif failure.check(TimeoutError, TCPTimeOutError ):

            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)




        


    
