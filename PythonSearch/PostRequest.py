#!/usr/bin/env python

import urllib2
import urllib
import base64
import json
import xml
import sys
import pprint

def post():

	url = 'https://gnip-api.twitter.com/search/fullarchive/accounts/greg-students/prod.json'
	UN = 'austin.griffith@colorado.edu'
	PWD = 'Vicki1957!'

	rule = 'raining'

	#query = '{"query":"' + rule + '", "maxResults":"10"}'

	query = '{"query":"' + rule + '", "fromDate":"201804150000", "toDate":"201804160000", "maxResults":"10"}'

	# query = '{"query":"' + rule + '","publisher":"twitter"}'


	base64string = base64.encodestring('%s:%s' % (UN, PWD)).replace('\n', '')
	req = urllib2.Request(url=url, data=query)
	req.add_header('Content-type', 'application/json')
	req.add_header("Authorization", "Basic %s" % base64string)

	try:
		response = urllib2.urlopen(req)
	except urllib2.HTTPError as e:
		pprint.pprint(e.read())
	the_page = response.read()
	pprint.pprint(the_page)

if __name__ == "__main__":
        post()
