
def find( substr, infile, outputfile ):

    with open(infile) as a, open(outputfile, 'w' ) as b:

        for line in a: 

            if substr in line: 

                b.write(line + '\n' )


#find('fromInstitutionId=9901', 'my_links.txt', 'UWIndependentLearning.txt' )
#find('fromInstitutionId=4672', 'my_links.txt', 'UWLaCrosse.txt' )
#find('fromInstitutionId=4656', 'my_links.txt', 'UWMadison.txt' )
#find('fromInstitutionId=4658', 'my_links.txt', 'UWMilwaukee.txt' )
#find('fromInstitutionId=4674', 'my_links.txt', 'UWOshkosh.txt' )
#find('fromInstitutionId=4690', 'my_links.txt', 'UWParkside.txt' )
#find('fromInstitutionId=4676', 'my_links.txt', 'UWPlatteville.txt' )
#find('fromInstitutionId=4678', 'my_links.txt', 'UWRiverFalls.txt' )
#find('fromInstitutionId=4680', 'my_links.txt', 'UWStevensPoint.txt')
#find('fromInstitutionId=4652', 'my_links.txt', 'UWStout.txt')
#find('fromInstitutionId=4682', 'my_links.txt', 'UWSuperior.txt')
#find('fromInstitutionId=4684', 'my_links.txt', 'UWWhitewater.txt')
#find('fromInstitutionId=4593', 'my_links.txt', 'BlackhawkTechCollege.txt')
#find('fromInstitutionId=4581', 'my_links.txt', 'ChippewaValleyTechCollege.txt')
#find('fromInstitutionId=4556', 'my_links.txt', 'FoxValleyTechCollege.txt')
#find('fromInstitutionId=4584', 'my_links.txt', 'GatewayTechCollege.txt')
#find('fromInstitutionId=4650', 'my_links.txt', 'LakeshoreTechCollege.txt')
#find('fromInstitutionId=4615', 'my_links.txt', 'MadisonAreaTechCollege.txt')
#find('fromInstitutionId=4683', 'my_links.txt', 'MidStateTechCollege.txt')
#find('fromInstitutionId=4614', 'my_links.txt', 'MilwaukeeAreaTechCollege.txt')
#find('fromInstitutionId=4583', 'my_links.txt', 'MidStateTechCollege.txt')
#find('fromInstitutionId=4614', 'my_links.txt', 'MilwaukeeAreaTechCollege.txt')
#find('fromInstitutionId=4583', 'my_links.txt', 'MoraineParkTechCollege.txt')
#find('fromInstitutionId=4646', 'my_links.txt', 'NicoletAreaTechCollege.txt')
#find('fromInstitutionId=4663', 'my_links.txt', 'NorthcentralTechCollege.txt')
#find('fromInstitutionId=4585', 'my_links.txt', 'NortheastWisTechCollege.txt')
#find('fromInstitutionId=4639', 'my_links.txt', 'SouthwestWisTechCollege.txt')
#find('fromInstitutionId=4671', 'my_links.txt', 'WaukeshaCountyTechCollege.txt')
#find('fromInstitutionId=4573', 'my_links.txt', 'WesternTechCollege.txt')
#find('fromInstitutionId=4599', 'my_links.txt', 'WisIndianheadTechCollege.txt')
find('fromInstitutionId=4688', 'my_links.txt', 'UWGreenBay.txt')




















