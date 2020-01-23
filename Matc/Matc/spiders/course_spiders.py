from scrapy import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.linkextractors import LinkExtractor
from scrapy.utils.markup import remove_tags
from Matc.items import MatcItem


class MatcSpider( CrawlSpider ):

    name = 'matc1'

    allowed_domains = ['madisoncollege.edu']

    start_urls = [ 

            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001211/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001213/DEGR/2017-05-30',
            'https://my.madisoncollege.edu/app/catalog/showCourse/MATC1/001215/DEGR/2018-05-29',
            ]

    rules = (

            Rule( LinkExtractor( allow=(r'app/catalog/showCourse/MATC1/')
                
                ),
                callback = 'parse_item',
                follow = True
                
                ),
            )

    def parse_item( self, response ):

        items = MatcItem() 
        #course_elements = response.xpath('div[@class="main"]')
    
        items['title'] = response.xpath('//div[@class="strong section-body"]/text()').extract_first()
        items['description'] = response.xpath('//div[@class="section-body"]/text()').extract_first()
        items['unit'] =  response.xpath('////div[@class="pull-right"]/div/text()').extract()[1]
        items['courses'] = response.xpath('////div[@class="pull-right"]/div/text()').extract()[2]
        items['prerequisites'] = response.xpath('////div[@class="pull-right"]/div/text()').extract()[5]

        yield items
