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
import pandas as pd

import datetime

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



# word "word" (word) -noword (#word) (from:word) (to:word) (@word) min_replies:1 min_faves:1 min_retweets:1 lang:es until:2022-12-01 since:2022-01-01
# word_qry = 'ayurveda'
# date_since = "2022-01-01"
# date_until = "2022-12-10"
# query = "#%s -is:retweet since:%s until:%s" % (word_qry, date_since, date_until)

#Initiate API and search

def tweetAPI(query):
    ''' 
    Method that returns raw Tweet list
    
    No input variables
    '''
    twapi = tweepy.API(auth)
    tweetsRaw = twapi.search_tweets(query, count = 1000, tweet_mode = 'extended')
    return tweetsRaw

# create dataframe from 
def tweetDF(tweetsRaw:list ) -> pd.DataFrame:
    columns = ['Time', 'User', 'Tweet ID', 'Tweet FULL']
    data = []
    for tweet in tweetsRaw:
        try:
            text = tweet.retweeted_status.full_text 
        except AttributeError: 
            text = tweet.full_text
        data.append([tweet.created_at, tweet.user.screen_name, tweet.id, text])

    tweetdf = pd.DataFrame(data, columns=columns)
    return tweetdf

# Get today date and time, so you can add to file
def now_datetime():
        return time.strftime("%Y%m%d-%H%M%S")