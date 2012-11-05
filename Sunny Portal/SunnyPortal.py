import urllib2, cookielib
from ClientForm import ParseResponse
class SunnyPortal:
    def __init__(self):
            self.url='https://www.sunnyportal.com/Templates/Start.aspx'
            cookiejar = cookielib.LWPCookieJar()
            cookiejar = urllib2.HTTPCookieProcessor(cookiejar)
            opener = urllib2.build_opener(cookiejar)
            urllib2.install_opener(opener)

    def login(self):
        response = urllib2.urlopen(self.url)
        forms = ParseResponse(response)
        form = forms[0]
        try:
            form['_ctl0:ContentPlaceHolder1:Logincontrol1:UserName']='FakeUsername'
            form['_ctl0:ContentPlaceHolder1:Logincontrol1:Password']='FakePassword'
        except Exception, e:
            print 'The following error occured:',e
            print 'URL='+self.url
        self.page=urllib2.urlopen(form.click('_ctl0:ContentPlaceHolder1:Logincontrol1:LoginBtn'))
        ##print self.page

    def download(self):
        self.login()
        response = urllib2.urlopen('https://www.sunnyportal.com/Templates/UserPlantList.aspx')
        forms = ParseResponse(response)
        form = forms[0]
        try:
            file=urllib2.urlopen(form.click('_ctl0:ContentPlaceHolder1:ImageButtonDownload')).read()
        except Exception, e:
            print 'Error while downloading the file:',e
        try:
            f=open('plantList.csv','w')
            f.write(file)
            f.close()
        except Exception, e:
            print 'Error while writing the file to disk:',e

SP=SunnyPortal()
SP.download()
print 'Execution finished'
