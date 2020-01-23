

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

    name = 'plateville_links7'


    allowed_domains = ['uwplatt.edu']

    start_urls = [


 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/A/AGINDUS/GRAD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/A/AGSCI/GRAD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/A/ART/GRAD",
 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/M/MATH/GRAD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/M/MEDIA/GRAD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/M/MUAP/GRAD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/M/MUSIC/GRAD",
 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/P/PHLSPHY/GRAD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/P/PHSC/GRAD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/P/PHYSICS/GRAD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/P/POLISCI/GRAD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/P/PSYCHLGY/GRAD",
 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/G/GEOGRPHY/GRAD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/G/GEOLOGY/GRAD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/G/GERMAN/GRAD",
 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/E/ECONOMIC/GRAD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/E/ENGLISH/GRAD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/E/ETHNSTDY/GRAD",
 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/C/CHEMSTRY/GRAD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/C/COMPUTER/GRAD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/C/COUNSED/GRAD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/C/CRIMLJUS/GRAD",
 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/H/HHP/GRAD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/H/HISTORY/GRAD",
 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/B/BIOLOGY/GRAD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/B/BUSADMIN/GRAD",
 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/S/SOCIOLGY/GRAD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/S/SPANISH/GRAD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/S/SPEECH/GRAD",
 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/T/TEACHING/GRAD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/T/THEATRE/GRAD",


 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/C/COUNSED/XGR", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/C/CRIMLJUS/XGR",

 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/I/INDUSTDY/XGR", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/I/ISCM/XGR",


 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/P/PHLSPHY/XGR", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/P/POLISCI/XGR", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/P/PROJMGT/XGR", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/P/PSYCHLGY/XGR",

 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/B/BIOLOGY/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/B/BUSADMIN/UGRD",
 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/A/ACCTING/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/A/AGBUS/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/A/AGEDUC/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/A/AGET/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/A/AGRIC/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/A/ANSCI/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/A/APC/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/A/ART/UGRD",
 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/C/CHEMSTRY/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/C/CHINESE/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/C/CIVILENG/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/C/COMPUTER/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/C/COUNSPSY/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/C/CR-SPAN/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/C/CRIMLJUS/UGRD",
 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/E/ECONOMIC/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/E/ELECTENG/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/E/ENERGY/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/E/ENGLISH/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/E/ENGRPHYS/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/E/ENTRP/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/E/ENVENG/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/E/ENVHORT/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/E/ESL/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/E/ETHNSTDY/UGRD",
 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/I/INDSTENG/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/I/INDUSTDY/UGRD",

 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/F/FORENSIC/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/F/FRENCH/UGRD",

 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/G/GENENG/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/G/GEOGRPHY/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/G/GEOLOGY/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/G/GERMAN/UGRD",
 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/M/MATH/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/M/MECHENG/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/M/MEDIA/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/M/MSNT/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/M/MUAP/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/M/MUSIC/UGRD",

 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/P/PHLSPHY/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/P/PHSC/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/P/PHYSICS/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/P/POLISCI/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/P/PORTUG/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/P/PSYCHLGY/UGRD",
 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/T/TEACHING/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/T/THEATRE/UGRD",

 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/S/SCSCI/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/S/SEJ/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/S/SOCIOLGY/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/S/SOFTWARE/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/S/SPANISH/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/S/SPEECH/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/S/STAT/UGRD",
 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/B/BIOLOGY/XUG", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/B/BUSADMIN/XUG",
 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/H/HHP/UGRD", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/H/HISTORY/UGRD",

 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/A/ACCTING/XUG", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/A/APC/XUG",

 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/E/ECONOMIC/XUG", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/E/ENERGY/XUG", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/E/ETHNSTDY/XUG",
 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/G/GENENG/XUG", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/G/GEOGRPHY/XUG",



 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/C/CIVILENG/XUG", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/C/COMPUTER/XUG", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/C/CRIMLJUS/XUG",

 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/I/INDSTENG/XUG", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/I/INDUSTDY/XUG",




 "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/M/MATH/XUG", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/M/MECHENG/XUG", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/M/MEDIA/XUG", "https://passexpress.uwplatt.edu/app/catalog/listCoursesBySubject/UWPLT/M/MUSIC/XUG",




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


