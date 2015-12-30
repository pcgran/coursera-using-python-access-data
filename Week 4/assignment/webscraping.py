import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# List of <a> tags
tags = soup('a')

index = 0
for tag in tags:
    index += 1
    print index, " - ", tag.get('href', None)
