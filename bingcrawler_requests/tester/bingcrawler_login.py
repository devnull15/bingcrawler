#!/usr/bin/python

import requests

rcounter = 0

def printr(r):
    global rcounter
    print 'URL: ' + r.url
    print 'Status: ' + str(r.status_code)
    print 'History: ' + str(r.history)
    print
    print 'Headers: ' + str(r.headers)
    print
    print 'Cookies: ' + str(r.cookies)
    print
#    print 'Content: ' + r.text
    print '----------------------------------------------'
    fn = 'html_responses/' + str(rcounter) + '.html'
    with open(fn, 'w') as f:
        f.write(r.text)
    rcounter+=1

def getPPFT(ppft):
    ret = ppft.split()[4]
    ret = ret[7:]
    ret = ret[:-4]
    return ret


### Create session object for persistent cookies
s = requests.session()
###


### 0: initial GET
r = s.get('http://login.live.com')
printr(r)
###

### 1: POST sign-in

## Used to find POST URL for 'sign in' button
# i = 0
# for l in r.text.split(','):
#     if l.find('i19') > -1:
#         print str(i) + ': ' + l
#     i+=1

## Breaks up javascript form submission into a list for getting submission data
formList = r.text.split(',')

## Gets the appropriate POST URL from javascript lines
urlList = formList[63].split(':')
url = urlList[1] + ':' + urlList[2]
url = url.strip("'")

## Making the payload...
data = {}
data['loginfmt'] = 'tester20152016%40outlook.com' #loginfmt
data['login'] = 'tester20152016%40outlook.com' #login
data['passwd'] = 'dFke6%24027t*x5X%26Wo7K*pxVvullX30'#passwd
data['type'] = '11' #type
data['PPFT'] = getPPFT(formList[129]) #PPFT
data['PPSX'] = 'Pass' #PPSX
data['NewUser'] = '1'#NewUser
data['LoginOptions'] = '3' #LoginOptions
data['FoundMSAs'] = None #FoundMSAs
data['fspost'] = 0 #fspost
data['i2'] = '1' #i2
data['i16'] = '%7B%22navigationStart%22%3A1462540104015%2C%22unloadEventStart%22%3A1462540110968%2C%22unloadEventEnd%22%3A1462540110969%2C%22redirectStart%22%3A0%2C%22redirectEnd%22%3A0%2C%22fetchStart%22%3A1462540104017%2C%22domainLookupStart%22%3A1462540104017%2C%22domainLookupEnd%22%3A1462540104017%2C%22connectStart%22%3A1462540104017%2C%22connectEnd%22%3A1462540104017%2C%22requestStart%22%3A1462540104075%2C%22responseStart%22%3A1462540104030%2C%22responseEnd%22%3A1462540110967%2C%22domLoading%22%3A1462540110968%2C%22domInteractive%22%3A1462540111038%2C%22domContentLoadedEventStart%22%3A1462540111049%2C%22domContentLoadedEventEnd%22%3A1462540111050%2C%22domComplete%22%3A1462540111050%2C%22loadEventStart%22%3A1462540111050%2C%22loadEventEnd%22%3A0%' #i16
data['i17'] = '0'#i17
data['i18'] = '__DefaultLogin_Strings%7C1%2C__DefaultLogin_Core%7C1%2C' #i18
data['i19'] = '14492'#i19
data['i21'] = '0' #i21
data['i22'] = '0' #i22
data['i23'] = '0' #i23

r = s.post(url, data=data)
printr(r)
###
