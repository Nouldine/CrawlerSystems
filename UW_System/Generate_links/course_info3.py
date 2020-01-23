
import pandas as pd
import csv

main_link = 'https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId={}&toInstitutionId=[]&submit=Next+Step' 

main_link_2 = "https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId={}&reqType=C&toInstitutionId=[]&departmentId=//&submitButton=Match+All+Courses"

def connection():

         df =  pd.read_csv("test17.csv", dtype = {'department_id': object } )
         from_campus = df['from_campus_id']
         to_campus   = df['to_campus_id']
         department  = df['department_id']
        
         links_size = len(from_campus)

         track_index = 0

         while  track_index <  links_size:
        
            new_links = "https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FequivalencyReport.do%253Bjsessionid%253D30C9786C05193E7334833B7199E61DCD&tispage=2&fromField=nothingChanged&fromInstitutionId={}&reqType=C&toInstitutionId={}&departmentId={}&submitButton=Match+All+Courses".format(from_campus[ track_index ],to_campus[ track_index ],department[ track_index ] )

            print new_links

            track_index += 1


connection()
