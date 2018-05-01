#!/usr/bin/env python

import urllib2      #needed if you are running python2.7
import base64
import json
import xml
import sys

class RequestWithMethod(urllib2.Request):
    def __init__(self, url, method, headers={}):
        self._method = method
        urllib2.Request.__init__(self, url, headers)

    def get_method(self):
        if self._method:
            return self._method
        else:
            return urllib2.Request.get_method(self)

if __name__ == "__main__":

	url = 'https://gnip-api.twitter.com/search/fullarchive/accounts/greg-students/prod.json'
	UN = 'austin.griffith@colorado.edu'
	PWD = 'Vicki1957!'
	query = 'raining'

	queryString = url + '?publisher=twitter&query=' + query

	base64string = base64.encodestring('%s:%s' % (UN, PWD)).replace('\n', '')

	req = RequestWithMethod(queryString, 'GET')
	req.add_header("Authorization", "Basic %s" % base64string)

	try:
		response = urllib2.urlopen(req)
	except urllib2.HTTPError as e:
        	print(e.read())

	the_page = response.read()
	print(the_page)
