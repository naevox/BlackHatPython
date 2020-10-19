import urllib2

url = "http://google.com"

headers = {}
headers['User-Agent'] = "bob_bot"

request = urllib2.Request(url,headers=headers)
reponse = urllib2.urlopen(request)

print response.read