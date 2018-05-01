#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import fileinput
from gapi import *
import json
from pprint import *

# with open('dataTest.json', 'a') as file:
#     json_data = json.load(file.read())
#     pprint.pprint(file)
# pprint.pprint(json_data)
#
# data = json.load(open('dataTest.json'))
#
# pprint.pprint(data)

tweets = []

if __name__ == "__main__":

    tweets = gnip_search()

    #exec(open("./gnip_search.py -f"raining has:geo profile_country:us" -n500 -s'2018-04-010T12:00' json").read())
