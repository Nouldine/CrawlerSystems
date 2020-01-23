
stringToMatch = 'fromInstitutionId=9999'
matchedLine = ''

# Get line
def get_links():

    with open('my_links.txt', 'r') as file:

        for line in file:

            if stringToMatch in line:

                matchedLine = line
                
                break

    with open('specefic_links.txt', 'w' ) as file:

        file.write(matchedLine)


  
