### README ###
# Limites de la API:
# https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/api-reference/get-search-tweets
##
# Requests / 15-min window (user auth)  180
# Requests / 15-min window (app auth)   450
#

#pip install tweepy
#pip install configparser
#pip install pandas

import configparser
import tweepy
import time

# # read config
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authenticate
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

# public_tweets = api.home_timeline()
#print(public_tweets)


timestr = time.strftime("%Y%m%d-%H%M%S")

"""
If you don't understand search queries, there is an excellent introduction to it here: 
https://github.com/twitterdev/getting-started-with-the-twitter-api-v2-for-academic-research/blob/main/modules/5-how-to-write-search-queries.md
"""

# Get tweets that contain the hashtag #petday
# -is:retweet means I don't want retweets
# lang:en is asking for the tweets to be in english

twapi = tweepy.API(auth)

# word "word" (word) -noword (#word) (from:word) (to:word) (@word) min_replies:1 min_faves:1 min_retweets:1 lang:es until:2022-12-01 since:2022-01-01
word_qry = 'ayurveda'
date_since = "2022-01-01"
date_until = "2022-12-10"
query = "#%s -is:retweet since:%s until:%s" % (word_qry, date_since, date_until)

def searchTweets(fullQuery):
    
    tw_df = []
    tweetsData = twapi.search_tweets(fullQuery, count = 1000, tweet_mode = 'extended')
    
    for tweet in tweetsData:
        try:
            text = tweetsData.retweeted_status.full_text 
        except AttributeError: 
            text = tweetsData.full_text
        tw_df.append([tweetsData.created_at, tweetsData.user.screen_name, tweetsData.id, text])
        
        return (tw_df | safe)


import pandas as pd

# create dataframe


df = pd.DataFrame(tw_df, columns=columns)

import datetime
def _getToday():
        return datetime.date.today().strftime("%Y%m%d")
# outpath = r'C:\test'
filename = "%s-%s.%s" % (word_qry, timestr ,"csv")

df.to_csv(filename)