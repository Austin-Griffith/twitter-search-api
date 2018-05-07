#!/usr/bin/python

# from secrets import *
# import ipdb
import searchtweets
import json
import pprint
from searchtweets import *
import datetime
from itertools import chain
########trying to use tweet_parser library to filter the json payload#####
from tweet_parser.tweet import Tweet
from tweet_parser.tweet_parser_errors import NotATweetError
import fileinput

now = datetime.datetime.now()
currentDate = now.strftime("%Y%m%d%H%M")
# print(now.strftime("%Y%m%d%H%M"))

# base_url = 'http://localhost:8000'

enterprise_search_args = load_credentials('creds.yaml', yaml_key='search_tweets_enterprise', env_overwrite=False)

# gen_rule_payload is a function to format filter rules for API calls but will not accept the args we need to filter
#rule = gen_rule_payload("is raining", "has:geo", from_date="2018-04-15", to_date="2018-04-16", results_per_call=100)

#this is the rule filter we should start with to catch ppl talking about rain by location
rule = {"query":"lang:en has:geo place_country:us", "maxResults":500, "toDate": "201805010000", "fromDate": "201801010000"}

tweets = collect_results(rule,
                         max_results=10000,
                         result_stream_args=enterprise_search_args)

rs = ResultStream(rule_payload=rule,
                  max_results=500,
                  max_pages=1,
                  **enterprise_search_args)

# data = [{
#     'tweet': {
#         'tweet_date': tweet['created_at'],
#         'place': tweet['place']['full_name'],
#         'tweet_text': tweet['text']
#     },
#     'user': {
#         'user_date': tweet['user']['created_at'],
#         'screen_name': tweet['user']['screen_name'],
#         'twitter_id': tweet['user']['id']
#     }
# } for tweet in tweets]


#format for Josh's visuals
# data = [{
#     'tweet': {
#         'tweet_date': tweet['created_at'],
#         'place': tweet['place']['full_name']
#     }
# } for tweet in tweets]

# pprint.pprint(data)

print('')
print('')
print("Length with location : %d" % len (data))
print('')
print('')
print("Length of total : %d" % len (tweets))

# #
with open('2018_data.json', 'w') as outfile:
      json.dump(data, outfile, sort_keys=True, indent=4)
