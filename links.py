import urllib2
import re

#connect to a URL
url = raw_input("Enter a url:  ")
website = urllib2.urlopen(url)

#read html code
html = website.read()

#use re.findall to get all the links
links = re.findall('"((http|ftp)s?://.*?)"', html)

for link in links:
    print link[0]
