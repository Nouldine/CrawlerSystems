
import pandas as pd
import os


# MadisonAreaTechCollege.csv        d
# MidStateTechCollege.csv           d
# MilwaukeeAreaTechCollege.csv      d
# MoraineParkTechCollege.csv        d
# NicoletAreaTechCollege.csv        d
# NorthcentralTechCollege.csv       d
# NortheastWisTechCollege.csv       d
# SouthwestWisTechCollege.csv       d
# uw_branch_campus.csv              d
# uw_eau_clair.csv                  d
# UWIndependentLearning.csv         d
# UWLaCrosse.csv                    d
# UWMadison.csv                     d             
# UWMilwaukee.csv                   d
# UWOshkosh.csv                     d
# UWParkside.csv                    d
# UWPlatteville.csv                 d
# UWRiverFalls.csv                  d
# UWStevensPoint.txt.csv            d
# UWSuperior.csv                    d
# UWWhitewater.csv                  d
# WaukeshaCountyTechCollege.csv     d
# WesternTechCollege.csv            d
# WisIndianheadTechCollege.csv      d


direct = 'uw_greenBay'

def read_files():

    for file_name in os.listdir(direct): 

        if file_name.endswith(".csv"): 

        #data = open(file_name)
            data = pd.read_csv(file_name)

            df = pd.DataFrame( data, columns = [ 'to', 'level' ,'credits' , 'course_2' ,'title_2','course_1','from_','gen_ed','title_1','special'] )

            find = ['UW Branch Campus', 'UW-Eau Claire', 'UW-Green Bay', 'UW-Independent Learning', 'UW-La Crosse', 'UW-Madison', 'UW-Milwaukee', 'UW-Oshkosh', 'UW-Parkside', 'UW-Platteville', 'UW-River Falls', 'UW-Stevens Point', 'UW-Stout', 'UW-Superior', 'UW-Whitewater', 'Blackhawk Tech. College', 'Chippewa Valley Tech. College', 'Fox Valley Tech. College', 'Gateway Tech. College', 'Lakeshore Tech. College', 'Madison Area Tech. College', 'Mid-State Tech. College', 'Milwaukee Area Tech. College', 'Moraine Park Tech. College', 'Nicolet Area Tech. College', 'Northcentral Tech. College', 'Northeast Wis. Tech. College', 'Southwest Wis. Tech. College', 'Waukesha County Tech. College', 'Western Tech. College', 'Wis. Indianhead Tech. College']

            replace_campus = ['9999', '4670', '4688', '9901', '4672', '4656', '4658', '4674', '4690', '4676', '4678', '4680', '4652', '4682', '4684', '4593', '4581', '4556', '4584', '4650', '4615', '4683', '4614', '4583', '4646', '4663', '4585', '4639', '4671', '4573', '4599']

            col = 'to'

            df[ col ] = df[col].replace( find, replace_campus )

            col2 = 'from_'

            df[ col2 ] = df[col2].replace( find, replace_campus )

            df.to_csv('uw/' + file_name, sep = ',', encoding='utf-8', index= False )

read_files()


