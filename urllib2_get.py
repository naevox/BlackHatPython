import urllib2

body = urllib2.urlopen("http://google.com")

print body.read()