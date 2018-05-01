from tweet_parser.tweet import Tweet
from tweet_parser.tweet_parser_errors import NotATweetError
import fileinput
import json
import pprint

for line in fileinput.FileInput("dataTest.json"):
    print(line)
    try:
        tweet_dict = json.loads(line)
        print(tweet_dict)
        tweet = Tweet(tweet_dict)
        print(tweet)
    except (json.JSONDecodeError,NotATweetError):
        pass
    print(tweet.created_at_string, tweet.all_text)
