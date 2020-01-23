

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
from automate_links.items import AutomateLinksItem


class  campus_links( scrapy.Spider ):

    name = "campus_info1"
    allowed_domains = ['wisconsin.edu']

    start_urls = [ 
            "https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9999&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4675&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4670&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4653&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4673&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4687&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4688&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4692&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4693&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4695&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=9901&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4672&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4656&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4658&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4659&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4698&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4674&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4676&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4657&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4634&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4678&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4680&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4697&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4696&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4652&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4682&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4684&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4689&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4593&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4581&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4556&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4584&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4650&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4615&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4683&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4614&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4583&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4646&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4663&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4585&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4639&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4671&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4573&toInstitutionId=4599&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=9999&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4675&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4670&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4653&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4673&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4687&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4688&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4692&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4693&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4695&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=9901&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4672&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4656&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4658&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4659&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4698&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4674&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4690&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4676&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4657&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4634&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4678&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4680&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4697&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4696&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4652&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4682&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4684&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4689&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4593&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4581&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4556&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4584&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4650&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4615&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4683&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4614&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4583&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4646&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4663&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4585&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4639&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4671&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4573&submit=Next+Step",

"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4599&toInstitutionId=4599&submit=Next+Step",

            ]


    def start_requests( self ):

        for u in self.start_urls:

            yield scrapy.Request( u, callback = self.parse_httpin, 
                    errback = self.errback_httpbin,
                    dont_filter = True )

    def parse_httpin( self, response ):

        # from_campus_name    = scrapy.Field()
        # to_campus_name      = scrapy.Field()
        # from_campus_id      = scrapy.Field()
        # to_campus_id        = scrapy.Field()
        # department_id       = scrapy.Field()

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




















