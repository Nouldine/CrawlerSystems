
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
from UW_Milwaukee.items import UwMilwaukeeItem

class Milwaukee_courses( CrawlSpider ):

    name = 'milwaukee'
    allowed_domains = ['uwm.edu']
    
    start_urls = [

            "https://catalog.uwm.edu/courses/"

            ]

    rules = (

            Rule( LinkExtractor( allow = (r'https://catalog.uwm.edu/courses/')),

                callback = 'parse_httpbin',

                follow = True

                ),

            )

    def parse_httpbin( self, response ):

        #self.logger.info("Got successful response {}".format(response.url))

        #items = UwMilwaukeeItem()
        
        #course = response.css('.courseblocktitle.noindent >  strong::text').extract_first()
        #course = response.css('.courseblocktitle.noindent >  strong::text').extract()
        courses =  response.xpath('//div[@class="courseblock"]/p/@aria-controls').extract()
        title = response.css('.courseblocktitle.noindent >  strong::text').extract() 
        #unit = response.xpath('////div[@class="courseblock"]/div/p/text()').extract_first()
        #unit = response.xpath('////div[@class="courseblock"]/div/p/text()').extract()
        unit = response.xpath('////div[@class="courseblock"]/div/p[1]/text()').extract()

        #description =  response.xpath('////div[@class="courseblock"]/div/p[@class="courseblockdesc noindent"]/text()').extract_first()
        #description =  response.xpath('////div[@class="courseblock"]/div/p[@class="courseblockdesc noindent"]/text()').extract()
        description = response.xpath('////div[@class="courseblock"]/div/p[2]/text()').extract()

        #prerequisites = response.xpath('////div[@class="courseblock"]/div/p/text()').extract()[3]
        prerequisites = response.xpath('////div[@class="courseblock"]/div/p[3]').extract()
        
        course_size = len(courses)

        final_courses = []
        final_prerequisites = []
        final_title = []
        final_unit = []
        final_description = []

        for course_set in courses:

            if course_set == '\n' or course_set == ' ' or course_set == '\t\t\t\t':
                continue
            final_courses.append(remove_tags(course_set))

        for prerequisites_set in prerequisites:

            if prerequisites_set == '\n' or prerequisites_set == ' ' or  prerequisites_set == '\t\t\t\t' :
                continue
            final_prerequisites.append(remove_tags(prerequisites_set))

        for title_set in title:

            if title_set == '\n' or title_set == ' ' or  title_set == '\t\t\t\t':
                continue
            final_title.append(remove_tags(title_set))

        for unit_set in unit:

            if unit_set == '\n' or unit_set == ' ' or unit_set == '\t\t\t\t':
                continue
            final_unit.append(remove_tags(unit_set))

        for description_set in description:

            if description_set == '\n' or description_set == ' ' or description_set == '\t\t\t\t':
                continue
            final_description.append(remove_tags(description_set))

        track_index = 0
        items = []

        while track_index < course_size:

            item = UwMilwaukeeItem()

            item['course'] = final_courses[ track_index ]
            item['title'] = final_title[ track_index ]
            item['unit'] = final_unit[ track_index ]
            item['description'] = final_description[ track_index ]
            item['prerequisites'] = final_prerequisites[ track_index ].strip()

            items.append(item)
            track_index += 1


        return items




























