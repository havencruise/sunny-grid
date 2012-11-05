import IEC,cookielib,urllib2
from ClientForm import ParseResponse

class untitled:
    def __init__(self): 
        cookiejar = cookielib.LWPCookieJar()
        cookiejar = urllib2.HTTPCookieProcessor(cookiejar)
        opener = urllib2.build_opener(cookiejar)
        urllib2.install_opener(opener)
        self.url='https://mycar.v2green.com/LogIn.jsp'
        self.page=''
        self.username='FakeUsername'
        self.password='FakePassword'
    def login(self):
##        response=urllib2.urlopen(self.url)
##        forms=ParseResponse(response)
##        form=forms[0]
        ie=IEC.IEController()
        ie.Navigate('https://mycar.v2green.com/LogIn.jsp')
        ie.SetInputValue('Username','FakeUsername')
        ie.SetInputValue('Password','FakePassword')
        #ie.SubmitForm()
        print IEC.IEController(window_url='https://mycar.v2green.com/DataAnalyst.jsp').GetDocumentText()

##        pop = IEC.IEController(window_url='https://mycar.v2green.com/DataAnalyst.jsp')
##        print pop.GetDocumentText()
        
        
    def download(self):
        self.login()
        ie=IEC.IEController()
        ie.Navigate('https://mycar.v2green.com/DataAnalyst.jsp')
        
unt=untitled()
unt.download()
