import urllib2,cookielib
from DOMForm import ParseResponse

cookiejar = cookielib.LWPCookieJar()
cookiejar = urllib2.HTTPCookieProcessor(cookiejar)
opener = urllib2.build_opener(cookiejar)
response = urllib2.urlopen("https://mycar.v2green.com/LogIn.jsp")
window = ParseResponse(response)
window.document  # HTML DOM Level 2 HTMLDocument interface
forms = window._htmlforms  # list of objects supporting ClientForm.HTMLForm i/face
form = forms[0]
form['UserName']='FakeUsername'
form['Password']='FakePassword'
loggedIn=urllib2.urlopen(form.click())
print loggedIn.read()
