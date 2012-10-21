#!/usr/bin/env python2

import sys
from os.path import join, split, abspath

from urllib import urlencode
from urllib2 import urlopen, Request
from urlparse import urlparse, urlunparse

from logbook import Logger, RotatingFileHandler

from credentials import USERNAME, PASSWORD



def main():
    logger = Logger('Log')
    try:
        log_path = join(sys.argv[1], '%s.log' % USERNAME)
    except IndexError:
        log_path = join(split(abspath(__file__))[0], '%s.log' % USERNAME)

    # create the handler
    log_handler = RotatingFileHandler(log_path)
    # push the context object to the application stack
    log_handler.push_application()

    logger.info('NetworkManager has connected to UoM_WIFI.')

    # POST to
    FORM_ACTION = '/auth/index.html/u'

    TEST_URL = 'https://www.google.co.uk'

    # form data to POST
    FORM_DATA = {
        'user': USERNAME,
        'password': PASSWORD,
        'cmd': 'authenticate',
        'Login': 'Log In'
    }

    # try to navigate to Google
    logger.info('Opening test URL %s.' % TEST_URL)
    page = urlopen(TEST_URL)
    url = urlparse(page.url)

    # if we're  on *.google.* domain, it's all good and we carry on browsin'
    if 'google' in url.netloc:
        logger.info('Looks like %s is authenticated, bye-bye.' % USERNAME)
        sys.exit(0)

    # otherwise, let's build the URL to POST things to and add other necessary
    # information
    logger.info('Looks like %s is not authenticated.' % USERNAME)
    logger.info('Build the authentication URL.')
    POST_URL = urlunparse((url.scheme, url.netloc, FORM_ACTION, '', '', ''))

    logger.info('Building the request object.')
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
    # TODO: add some sensible verification, error checking and fallbacks
    logger.info('Trying to authenticate.')
    auth_page = urlopen(request)
    sys.exit(0)

if __name__ == '__main__':
    main()
