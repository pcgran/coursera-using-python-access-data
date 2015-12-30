import urllib
from BeautifulSoup import *

soup = BeautifulSoup(urllib.urlopen('http://python-data.dr-chuck.net/comments_217221.html').read())

# List of <a> tags
tags = soup('span')

total = 0
for tag in tags:
    total += int(tag.contents[0])

print 'Sum ', total
