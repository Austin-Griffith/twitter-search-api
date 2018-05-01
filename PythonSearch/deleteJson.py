#!/usr/bin/env python

import json
import pprint



with open('saleries.json', 'r') as json_data:

    tweet_data = json.load(json_data)
    pprint.pprint(tweet_data)
    print('\n')


# Iterate through the objects in the JSON and pop (remove)
# the obj once we find it.
# for i in range(len(tweet_data)):
#     if tweet_data[i]["year"] is not None:
#         tweet_data.pop(i)
#         print("popped item")
#         break

print('\n')

pprint.pprint(tweet_data)
