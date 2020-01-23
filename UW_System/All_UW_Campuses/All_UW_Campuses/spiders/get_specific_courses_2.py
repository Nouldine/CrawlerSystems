
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
from All_UW_Campuses.items import AllUwCampusesItem



class Matc_UW_Madison( scrapy.Spider ):

    name = 'courses'

    allowed_domains = ['wisconsin.edu']

    start_urls = [
		
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4688&departmentId=9196&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4688&departmentId=9307&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4688&departmentId=9504&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4688&departmentId=9510&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4688&departmentId=9514&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4688&departmentId=9527&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4688&departmentId=9530&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4688&departmentId=9531&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4688&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4688&departmentId=9802&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4688&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4688&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4688&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4658&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4658&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4658&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4658&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4658&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4672&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4672&departmentId=9501&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4672&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4672&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4672&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4672&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4656&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4656&departmentId=9307&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4656&departmentId=9501&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4656&departmentId=9510&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4656&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4656&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4656&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4656&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4674&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4674&departmentId=9101&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4674&departmentId=9307&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4674&departmentId=9501&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4674&departmentId=9504&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4674&departmentId=9522&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4674&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4674&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4674&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4674&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4676&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4676&departmentId=9101&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4676&departmentId=9104&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4676&departmentId=9105&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4676&departmentId=9114&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4676&departmentId=9116&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4676&departmentId=9307&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4676&departmentId=9504&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4676&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4676&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4676&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4676&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4678&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4678&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4678&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4678&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4678&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4690&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4690&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4690&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4690&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4690&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4680&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4680&departmentId=9307&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4680&departmentId=9501&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4680&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4680&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4680&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4680&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4684&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4684&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4684&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4684&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4684&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=9999&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4652&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4652&departmentId=9101&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4652&departmentId=9150&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4652&departmentId=9154&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4652&departmentId=9196&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4652&departmentId=9307&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4652&departmentId=9605&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4652&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4652&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4652&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4652&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4652&departmentId=9890&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4593&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4593&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4593&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4593&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4593&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4682&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4682&departmentId=9307&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4682&departmentId=9504&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4682&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4682&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4682&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4682&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4581&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4581&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4581&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4581&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4581&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4556&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4556&departmentId=9101&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4556&departmentId=9102&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4556&departmentId=9103&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4556&departmentId=9104&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4556&departmentId=9105&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4556&departmentId=9106&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4556&departmentId=9107&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4556&departmentId=9109&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4556&departmentId=9196&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4556&departmentId=9307&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4556&departmentId=9317&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4556&departmentId=9504&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4556&departmentId=9514&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4556&departmentId=9605&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4556&departmentId=9606&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4556&departmentId=9623&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4556&departmentId=9699&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4556&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4556&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4556&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4556&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4556&departmentId=9890&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4615&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4615&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4615&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4615&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4615&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4650&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4650&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4650&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4650&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4650&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4584&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4584&departmentId=9103&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4584&departmentId=9106&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4584&departmentId=9307&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4584&departmentId=9501&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4584&departmentId=9504&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4584&departmentId=9508&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4584&departmentId=9513&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4584&departmentId=9522&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4584&departmentId=9526&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4584&departmentId=9530&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4584&departmentId=9531&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4584&departmentId=9543&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4683&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4683&departmentId=9501&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4683&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4683&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4683&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4683&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4584&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4584&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4584&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4584&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4614&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4614&departmentId=9104&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4614&departmentId=9504&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4614&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4614&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4614&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4614&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4646&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4646&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4646&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4646&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4646&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4583&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4583&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4583&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4583&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4583&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4663&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4663&departmentId=9504&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4663&departmentId=9601&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4663&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4663&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4663&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4663&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4585&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4585&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4585&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4585&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4585&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4639&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4639&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4639&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4639&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4639&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4671&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4671&departmentId=9501&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4671&departmentId=9504&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4671&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4671&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4671&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4671&departmentId=9809&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4573&departmentId=nan&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4573&departmentId=9504&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4573&departmentId=9801&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4573&departmentId=9804&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4573&departmentId=9806&submitButton=Match+All+Courses",
"https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId=4599&reqType=C&toInstitutionId=4573&departmentId=9809&submitButton=Match+All+Courses",		

            ]


    def  start_requests( self ):

        for u in self.start_urls:

            yield scrapy.Request( u, callback = self.parse_httpbin,
                    errback = self.errback_httpbin,
                    dont_filter = True )


    def parse_httpbin( self, response ):

        self.logger.info("Got successful response {}".format(response.url) )

        #items = UwSystemItem()

        #course = response.css('#reportTable > tbody > tr > td.::text').extract()
        #course = response.css('tbody > tr > td::text').extract()
        #course = response.css('.campus-one-list::text').extract()[0];
        course_1  = response.xpath('////tr/td[1][@class="campus-one-list"]/text()').extract()
        title_1   = response.xpath('////tr/td[2][@class="campus-one-list"]/text()').extract()
        course_2  = response.xpath('////tr/td[3][@class="campus-two-list"]/text()').extract()
        title_2   = response.xpath('////tr/td[4][@class="campus-two-list"]/text()').extract()
        credits   = response.xpath('////tr/td[5][@class="campus-two-list"]/text()').extract()
        gen_ed    = response.xpath('////tr/td[6][@class="campus-two-list"]').extract()
        level     = response.xpath('////tr/td[7][@class="campus-two-list"]').extract()
        special   = response.xpath('////tr/td[8][@class="special-list"]').extract()
        from_camp = response.css('span#fromInst::text').extract_first()
        to_camp   = response.css('span#toDept::text').extract_first()

        final_course_1  = []
        final_title_1   = []
        final_course_2  = []
        final_title_2   = []
        final_credits   = []
        final_gen_ed    = []
        final_level     = []
        final_special   = []

        for  course_set1 in course_1:

            if course_set1 == '\n' or course_set1 == ' ':

                continue

            final_course_1.append(remove_tags(course_set1))

        for title1 in  title_1:

            if title1 == '\n' or title1 == ' ':

                continue

            final_title_1.append(remove_tags(title1))

        for course_set2 in course_2:

            if course_set2 == '\n' or  course_set2 == ' ':

                continue

            final_course_2.append(remove_tags(course_set2))

        for title2 in title_2:

            if title2 == '\n' or title2 == ' ':

                continue

            final_title_2.append(remove_tags(title2))

        for creditset in credits:

            if creditset == '\n' or creditset == ' ':

                continue

            final_credits.append(remove_tags(creditset))

        for gen in gen_ed:

            if gen == '\n':

                continue

            final_gen_ed.append(remove_tags(gen))

        for lev in level:

            if lev == '\n' or lev == ' ':
                continue

            final_level.append(remove_tags(lev))

        for specia in special:

            if specia == '\n\n                ':

                continue

            final_special.append(remove_tags(specia))

        item = []
        track_index = 0
        course_size = len(final_course_1)

        while track_index < course_size:

            items = AllUwCampusesItem()


            items['course_1']  = final_course_1[ track_index ].strip()
            items['title_1']   = final_title_1[ track_index ].strip()
            items['course_2']  = final_course_2[ track_index ].strip()
            items['title_2']   = final_title_2[ track_index ].strip()
            items['credits']   = final_credits[ track_index ].strip()
            items['from_']     = from_camp
            items['to']        = to_camp

            try:

                items['gen_ed']    = final_gen_ed[ track_index ].strip()

            except IndexError:

                items['gen_ed']    = 'None'

            try:
                items['level']     = final_level[ track_index ].strip()

            except IndexError:

                items['level'] = 'None'

            try:
                items['special']   = final_special[ track_index ].strip()

            except IndexError:

                items['special']   = 'None'

            item.append(items)

            track_index += 1

        return item


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

