import urllib,urllib2,cookielib
from ClientForm import  ParseResponse
import DOMForm
import xml.dom.ext

class GridPoint:
    def __init__(self): 
        cookiejar = cookielib.LWPCookieJar()
        cookiejar = urllib2.HTTPCookieProcessor(cookiejar)
        opener = urllib2.build_opener(cookiejar)
        urllib2.install_opener(opener)
        self.url='https://mycar.v2green.com/LogIn.jsp'
        self.page=''
        self.username='NYIT-analyst'
        self.password='DrumBeat!'
    def login(self):
        response=urllib2.urlopen(self.url)
        forms=ParseResponse(response)
        form=forms[0]
##        print form
        try:
            form['UserName']=self.username
            form['Password']=self.password
        except Exception,e:
            print 'The following error occured:',e
        self.page=urllib2.urlopen(form.click())

    def download(self):
        self.login()
        print self.page.geturl()
        response=urllib2.urlopen(self.page.geturl())
        window = DOMForm.ParseResponse(response)
        forms = window._htmlforms  # list of objects supporting ClientForm.HTMLForm i/face
        form = forms[0]
##        xml.dom.ext.XHtmlPrint(self.page,response)
        
        try:
            self.data=urllib2.urlopen(form.click()).read()
            print self.data
        except Exception, e:
            print 'Error downloading the file:',e
        try:
            f=open('rawData.csv','w')
            f.write(self.data)
            f.close()
        except Exception, e:
            print 'Error saving the file:',e

GP=GridPoint()
GP.download()
print 'Execution Finished'
