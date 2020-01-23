

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

    name = "campus_info1"
    allowed_domains = ['wisconsin.edu']

    start_urls = [ 
    
            #"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4690&submit=Next+Step", 
            "https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4684&submit=Next+Step"

            ]


    def start_requests( self ):

        for u in self.start_urls:

            yield scrapy.Request( u, callback = self.parse_httpin, 
                    errback = self.errback_httpbin,
                    dont_filter = True )

    def parse_httpin( self, response ):

        self.logger.info("Got successful response {}".format(response.url) )
         
        department_id = response.xpath('//select[@name="departmentId"]/option/@value').extract() 
        departmemt = response.xpath('//select[@name="departmentId"]/option/text()').extract()

        from_institution_final  = []
        institution_name = []

        item = [] 
        track_index = 0
        vec_size = len(department_id)

        while track_index < vec_size:

            items = IdInfoItem()
            
            items['department_id'] = department_id[ track_index ].strip() 
            items['department'] = departmemt[ track_index ].strip()

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




















