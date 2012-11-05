import urllib,urllib2,cookielib,time
class Number3:
    def __init__(self):
            self.url='http://192.168.8.14/?command=NewestRecord&table=Status'
            cookiejar = cookielib.LWPCookieJar()
            cookiejar = urllib2.HTTPCookieProcessor(cookiejar)
            opener = urllib2.build_opener(cookiejar)
            urllib2.install_opener(opener)
    def download(self):
        self.page=urllib2.urlopen(self.url)
        print self.page.read()

num=Number3()
i=0
while(i<3):
    i=i+1
    num.download()