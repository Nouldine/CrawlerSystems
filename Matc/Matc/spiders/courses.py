from scrapy import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.linkextractors import LinkExtractor
from scrapy.utils.markup import remove_tags
from Matc.items import MatcItem


class MatcSpider( CrawlSpider ):

    name = 'matc'

    allowed_domains = ['www.madisoncollege.edu']

    start_urls = [ 

            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001211/DEGR/',
            
            #'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001213/DEGR/2017-05-30',
            #'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001215/DEGR/2018-05-29'
            ]

    rules = (

            Rule( LinkExtractor( allow=(
                
                r'/app/catalog/showCourse/MATC1/', 
                
                )),
                
                callback = 'parse_item',
                follow = True
                
                ),
            )

    def parse_item( self, response ):

        items = MatcItem() 
        
        title = response.css('section.main > section.no-outline-on-focus > div.section-content > div.strong.section-body::text').extract()
        description = response.css('section.main > section.no-outline-on-focus > div.section-cotent > div.section-body::text').extract()
        unit = response.css('section.main > section.no-outline-on-focus > div.section-content.clearfix > div.pull-right > div::text').extract()
        #courses = response.css('.main > div.section-content.clearfix > div.pull-right::text').extract()
        #items['course'] = course
        items['unit'] = unit
        items['title'] = title
        items['description'] = description

        yield items
