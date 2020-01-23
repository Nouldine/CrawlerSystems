

lst = {'Women','Men'}

url_test = 'http://www.Holiday.com/%s/Beach'

for i in lst:

    url = url_test %i

    print url
