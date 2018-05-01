#!/usr/bin/python

# from secrets import *
# import searchtweets
import ipdb
import json
import pprint
from searchtweets import *
import datetime
########trying to use tweet_parser library to filter the json payload#####
from tweet_parser.tweet import Tweet
from tweet_parser.tweet_parser_errors import NotATweetError
import fileinput

now = datetime.datetime.now()
print(now.strftime("%Y%m%d0000"))

enterprise_search_args = load_credentials("creds.yaml", yaml_key="search_tweets_enterprise", env_overwrite=False)

# gen_rule_payload is a function to format filter rules for API calls but will not accept the args we need to filter
#rule = gen_rule_payload("is raining", "has:geo", from_date="2018-04-15", to_date="2018-04-16", results_per_call=100)

#this is the rule filter we should start with to catch ppl talking about rain by location
#added place_country:us rule to filter tweets for only in US
rule = {"query": "\"is raining\" lang:en has:geo place_country:us", "maxResults":100, "toDate": "201804300000", "fromDate": "201804150000"}

print(rule)
print('\n')

tweets = collect_results(rule,
                         max_results=100,
                         result_stream_args=enterprise_search_args)

rs = ResultStream(rule_payload=rule,
                  max_results=100,
                  max_pages=1,
                  **enterprise_search_args)

#print(rs)
#[print(tweet.all_text, end='\n\n') for tweet in tweets[0:100]];

with open('tweet_data.json', 'w') as outfile:
      json.dump(tweets, outfile, sort_keys=True, indent=4)

################python script is working up to here######################
    #successfully dumps the tweets pulled from API to outfile called tweet_data.json

# only the need data from the tweet object stored in data variable 
data = [{
    'tweet': {
        'tweet_date': tweet['created_at'],
        'place': tweet['place']['full_name'],
        'tweet_text': tweet['text']
    },
    'user': {
        'user_date': tweet['user']['created_at'],
        'screen_name': tweet['user']['screen_name'],
        'twitter_id': tweet['user']['id']
    }
} for tweet in tweets]

pprint.pprint(data)
# pprint.pprint(tweets)
