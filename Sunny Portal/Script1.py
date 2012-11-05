import urllib2
self.page=urllib2.urlopen('https://mycar.v2green.com/DataAnalyst.jsp/html/head/script[10]')
print self.page.read()