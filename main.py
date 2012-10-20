#!/usr/bin/env python2

import sys

from urllib import urlencode
from urllib2 import urlopen, Request
from urlparse import urlparse, urlunparse

from credentials import USERNAME, PASSWORD

# POST to
FORM_ACTION = '/auth/index.html/u'

# form data to POST
FORM_DATA = {
    'user': USERNAME,
    'password': PASSWORD,
    'cmd': 'authenticate',
    'Login': 'Log In'
}

# try to navigate to Google
page = urlopen("https://www.google.co.uk")
url = urlparse(page.url)

# if we're  on *.google.* domain, it's all good and we carry on browsin'
if 'google' in url.netloc:
    print 'All good'
    sys.exit(0)

# otherwise, let's build the URL to POST things to and add other necessary
# information
POST_URL = urlunparse((url.scheme, url.netloc, FORM_ACTION, '', '', ''))

request = Request(POST_URL, urlencode(FORM_DATA))
request.add_header('Accept',
                   'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
request.add_header('Content-Type', 'application/x-www-form-urlencoded')
request.add_header('Origin', 'https://wireless.its.manchester.ac.uk')
request.add_header('Referer', url)
request.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux i686)'+
                   'AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94'+
                   'Safari/537.4')

# this call to urlopen POSTs the urlencoded FORM_DATA, along with the specified
# headers to POST_URL
auth_page = urlopen(request)

print auth_page.get_code()
