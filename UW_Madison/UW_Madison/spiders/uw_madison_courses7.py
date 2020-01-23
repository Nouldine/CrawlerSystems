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
from UW_Madison.items import UwMadisonItem

# CrawlSpider
class Madison_courses( scrapy.Spider ):

    name = 'uw_madison_final'

    allowed_domains = ['wisc.edu']

    start_urls = [
            
"http://guide.wisc.edu/courses/acct_i_s/",
"http://guide.wisc.edu/courses/act_sci/",
"http://guide.wisc.edu/courses/african/",
"http://guide.wisc.edu/courses/afroamer/",
"http://guide.wisc.edu/courses/a_a_e/",
"http://guide.wisc.edu/courses/agroecol/",
"http://guide.wisc.edu/courses/agronomy/",
"http://guide.wisc.edu/courses/a_f_aero/",
"http://guide.wisc.edu/courses/amer_ind/",
"http://guide.wisc.edu/courses/anatomy/",
"http://guide.wisc.edu/courses/anat_phy/",
"http://guide.wisc.edu/courses/anesthes/",
"http://guide.wisc.edu/courses/an_sci/",
"http://guide.wisc.edu/courses/anthro/",
"http://guide.wisc.edu/courses/art/",
"http://guide.wisc.edu/courses/art_ed/",
"http://guide.wisc.edu/courses/art_hist/",
"http://guide.wisc.edu/courses/asian_am/",
"http://guide.wisc.edu/courses/asian/",
"http://guide.wisc.edu/courses/asialang/",
"http://guide.wisc.edu/courses/astron/",
"http://guide.wisc.edu/courses/atm_ocn/",
"http://guide.wisc.edu/courses/biochem/",
"http://guide.wisc.edu/courses/bse/",
"http://guide.wisc.edu/courses/biology/",
"http://guide.wisc.edu/courses/biocore/",
"http://guide.wisc.edu/courses/b_m_e/",
"http://guide.wisc.edu/courses/bmolchem/",
"http://guide.wisc.edu/courses/b_m_i/",
"http://guide.wisc.edu/courses/botany/",
"http://guide.wisc.edu/courses/crb/",
"http://guide.wisc.edu/courses/cbe/",
"http://guide.wisc.edu/courses/chem/",
"http://guide.wisc.edu/courses/chicla/",
"http://guide.wisc.edu/courses/civ_engr/",
"http://guide.wisc.edu/courses/cscs/",
"http://guide.wisc.edu/courses/classics/",
"http://guide.wisc.edu/courses/cnp/",
"http://guide.wisc.edu/courses/com_arts/",
"http://guide.wisc.edu/courses/cs_d/",
"http://guide.wisc.edu/courses/c_e_soc/",
"http://guide.wisc.edu/courses/comp_bio/",
"http://guide.wisc.edu/courses/comp_lit/",
"http://guide.wisc.edu/courses/comp_sci/",
"http://guide.wisc.edu/courses/cnsr_sci/",
"http://guide.wisc.edu/courses/coun_psy/",
"http://guide.wisc.edu/courses/curric/",
"http://guide.wisc.edu/courses/dy_sci/",
"http://guide.wisc.edu/courses/dance/",
"http://guide.wisc.edu/courses/ds/",
"http://guide.wisc.edu/courses/e_a_stds/",
"http://guide.wisc.edu/courses/e_asian/",
"http://guide.wisc.edu/courses/econ/",
"http://guide.wisc.edu/courses/elpa/",
"http://guide.wisc.edu/courses/ed_psych/",
"http://guide.wisc.edu/courses/ed_pol/",
"http://guide.wisc.edu/courses/e_c_e/",
"http://guide.wisc.edu/courses/emer_med/",
"http://guide.wisc.edu/courses/e_m_a/",
"http://guide.wisc.edu/courses/e_p/",
"http://guide.wisc.edu/courses/e_p_d/",
"http://guide.wisc.edu/courses/esl/",
"http://guide.wisc.edu/courses/engl/",
"http://guide.wisc.edu/courses/entom/",
"http://guide.wisc.edu/courses/envir_st/",
"http://guide.wisc.edu/courses/fam_med/",
"http://guide.wisc.edu/courses/fisc/",
"http://guide.wisc.edu/courses/finance/",
"http://guide.wisc.edu/courses/folklore/",
"http://guide.wisc.edu/courses/food_sci/",
"http://guide.wisc.edu/courses/f_w_ecol/",
"http://guide.wisc.edu/courses/french/",
"http://guide.wisc.edu/courses/gen_ws/",
"http://guide.wisc.edu/courses/gen_bus/",
"http://guide.wisc.edu/courses/genetics/",
"http://guide.wisc.edu/courses/geog/",
"http://guide.wisc.edu/courses/g_l_e/",
"http://guide.wisc.edu/courses/geosci/",
"http://guide.wisc.edu/courses/german/",
"http://guide.wisc.edu/courses/gns/",
"http://guide.wisc.edu/courses/greek/",
"http://guide.wisc.edu/courses/hebr_bib/",
"http://guide.wisc.edu/courses/hebr_mod/",
"http://guide.wisc.edu/courses/history/",
"http://guide.wisc.edu/courses/hist_sci/",
"http://guide.wisc.edu/courses/hort/",
"http://guide.wisc.edu/courses/hdfs/",
"http://guide.wisc.edu/courses/h_oncol/",
"http://guide.wisc.edu/courses/i_sy_e/",
"http://guide.wisc.edu/courses/info_sys/",
"http://guide.wisc.edu/courses/integart/",
"http://guide.wisc.edu/courses/ils/",
"http://guide.wisc.edu/courses/integsci/",
"http://guide.wisc.edu/courses/inter_ag/",
"http://guide.wisc.edu/courses/interegr/",
"http://guide.wisc.edu/courses/inter_ls/",
"http://guide.wisc.edu/courses/inter_he/",
"http://guide.wisc.edu/courses/stdyabrd/",
"http://guide.wisc.edu/courses/intl_bus/",
"http://guide.wisc.edu/courses/intl_st/",
"http://guide.wisc.edu/courses/italian/",
"http://guide.wisc.edu/courses/jewish/",
"http://guide.wisc.edu/courses/journ/",
"http://guide.wisc.edu/courses/kines/",
"http://guide.wisc.edu/courses/pub_affr/",
"http://guide.wisc.edu/courses/land_arc/",
"http://guide.wisc.edu/courses/lca_lang/",
"http://guide.wisc.edu/courses/lca/",
"http://guide.wisc.edu/courses/lacis/",
"http://guide.wisc.edu/courses/latin/",
"http://guide.wisc.edu/courses/law/",
"http://guide.wisc.edu/courses/legal_st/",
"http://guide.wisc.edu/courses/l_i_s/",
"http://guide.wisc.edu/courses/lsc/",
"http://guide.wisc.edu/courses/linguis/",
"http://guide.wisc.edu/courses/littrans/",
"http://guide.wisc.edu/courses/m_h_r/",
"http://guide.wisc.edu/courses/marketng/",
"http://guide.wisc.edu/courses/m_s_e/",
"http://guide.wisc.edu/courses/math/",
"http://guide.wisc.edu/courses/m_e/",
"http://guide.wisc.edu/courses/md_genet/",
"http://guide.wisc.edu/courses/med_hist/",
"http://guide.wisc.edu/courses/m_m_i/",
"http://guide.wisc.edu/courses/med_phys/",
"http://guide.wisc.edu/courses/med_sc_m/",
"http://guide.wisc.edu/courses/med_sc_v/",
"http://guide.wisc.edu/courses/medicine/",
"http://guide.wisc.edu/courses/medieval/",
"http://guide.wisc.edu/courses/microbio/",
"http://guide.wisc.edu/courses/mil_sci/",
"http://guide.wisc.edu/courses/m_envtox/",
"http://guide.wisc.edu/courses/mol_biol/",
"http://guide.wisc.edu/courses/music/",
"http://guide.wisc.edu/courses/mus_perf/",
"http://guide.wisc.edu/courses/nav_sci/",
"http://guide.wisc.edu/courses/neursurg/",
"http://guide.wisc.edu/courses/neurol/",
"http://guide.wisc.edu/courses/neurodpt/",
"http://guide.wisc.edu/courses/ntp/",
"http://guide.wisc.edu/courses/n_e/",
"http://guide.wisc.edu/courses/nursing/",
"http://guide.wisc.edu/courses/nutr_sci/",
"http://guide.wisc.edu/courses/obs_gyn/",
"http://guide.wisc.edu/courses/occ_ther/",
"http://guide.wisc.edu/courses/oncology/",
"http://guide.wisc.edu/courses/otm/",
"http://guide.wisc.edu/courses/ophthalm/",
"http://guide.wisc.edu/courses/path_bio/",
"http://guide.wisc.edu/courses/path/",
"http://guide.wisc.edu/courses/pediat/",
"http://guide.wisc.edu/courses/phm_sci/",
"http://guide.wisc.edu/courses/phmcol_m/",
"http://guide.wisc.edu/courses/pharmacy/",
"http://guide.wisc.edu/courses/phm_prac/",
"http://guide.wisc.edu/courses/philos/",
"http://guide.wisc.edu/courses/phy_ther/",
"http://guide.wisc.edu/courses/phy_asst/",
"http://guide.wisc.edu/courses/physics/",
"http://guide.wisc.edu/courses/physiol/",
"http://guide.wisc.edu/courses/pl_path/",
"http://guide.wisc.edu/courses/poli_sci/",
"http://guide.wisc.edu/courses/pop_hlth/",
"http://guide.wisc.edu/courses/portug/",
"http://guide.wisc.edu/courses/psychiat/",
"http://guide.wisc.edu/courses/psych/",
"http://guide.wisc.edu/courses/publhlth/",
"http://guide.wisc.edu/courses/radiol/",
"http://guide.wisc.edu/courses/real_est/",
"http://guide.wisc.edu/courses/rhab_med/",
"http://guide.wisc.edu/courses/rp_se/",
"http://guide.wisc.edu/courses/relig_st/",
"http://guide.wisc.edu/courses/r_m_i/",
"http://guide.wisc.edu/courses/scand_st/",
"http://guide.wisc.edu/courses/sts/",
"http://guide.wisc.edu/courses/sr_med/",
"http://guide.wisc.edu/courses/slavic/",
"http://guide.wisc.edu/courses/s_a_phm/",
"http://guide.wisc.edu/courses/soc_work/",
"http://guide.wisc.edu/courses/soc/",
"http://guide.wisc.edu/courses/soil_sci/",
"http://guide.wisc.edu/courses/spanish/",
"http://guide.wisc.edu/courses/stat/",
"http://guide.wisc.edu/courses/surgery/",
"http://guide.wisc.edu/courses/surg_sci/",
"http://guide.wisc.edu/courses/theatre/",
"http://guide.wisc.edu/courses/univ_for/",
"http://guide.wisc.edu/courses/urb_r_pl/",
"http://guide.wisc.edu/courses/zoology/",
    ]
    
    def  start_requests( self ):

        for u in self.start_urls:
            
            yield scrapy.Request( u, callback = self.parse_httpbin,
                    errback = self.errback_httpbin,
                    dont_filter = True )


    def parse_httpbin( self, response ):

        self.logger.info("Got successful response {}".format(response.url) )
        courses = response.css('span.courseblockcode::text').extract() 
        prerequisites = response.xpath('//div[@class="cb-extras"]/p[1]/span[@class="cbextra-data"][1][last()]').extract()
        title = response.css('div.sc_sccoursedescs > div.courseblock > p.courseblocktitle > strong::text').extract()
        unit = response.css('.courseblockcredits::text').extract()
        description =  response.css('.courseblockdesc.noindent').extract()
        
        final_courses = [] 
        final_prerequisites = []
        final_title = []
        final_unit = []
        final_description = []

        for course_set in courses:

            if course_set == '\n' or course_set == ' ':
                continue
            final_courses.append(remove_tags(course_set))

        for prerequisites_set in prerequisites:

            if prerequisites_set == '\n' or prerequisites_set == ' ' or  prerequisites_set == '\t\t\t\t' :
                continue
        
            final_prerequisites.append(remove_tags(prerequisites_set))

        for title_set in title:

            if title_set == '\n' or title_set == ' ':
                continue 
            final_title.append(remove_tags(title_set))

        for unit_set in unit: 

            if unit_set == '\n' or unit_set == ' ':
                continue
            final_unit.append(remove_tags(unit_set))

        for description_set in description: 

            if description_set == '\n' or description_set == ' ':
                continue 
            final_description.append(remove_tags(description_set))

        course_size = len(final_courses)
        items = []
        track_index = 0
        
        print("Course_Size:", course_size )
        print("prerequisites_size", len(final_prerequisites))
        print("title_size", len(final_title))
        print("Unit_size", len(final_unit))
        print("description", len(final_description))

        while track_index < course_size:
          
            item = UwMadisonItem()

            item['course'] = final_courses[ track_index ]
            item['title'] = final_title[ track_index ]
            item['unit'] = final_unit[ track_index ]
            item['description'] = final_description[ track_index ]
            item['prerequisites'] =  final_prerequisites[ track_index ]

            #try:

                #item['prerequisites'] = final_prerequisites[ track_index ]
                #item['prerequisites'] = response.xpath('//div[@class="cb-extras"]/p/span[@class="cbextra-data"]/a[1]/@title[1]').extract()[ track_index ]

            #except IndexError:

                #item['prerequisites'] = 'None'

            items.append(item)
            track_index += 1
            
        return items

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



        
