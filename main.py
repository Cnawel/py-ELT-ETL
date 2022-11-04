import os
from tw_api_scrape1 import tweetAPI, tweetDF, now_datetime


if __name__ == "__main__":
    word_qry = 'enolaholmes'
    hashtag = 'enolaholmes'
    #date_since = "2022-01-01"
    date_since = "since:"
    date_until = "until:"
    #query = f"#{hashtag} {word_qry}-is:retweet {date_since} {date_until}"
    query = f"#{hashtag} -is:retweet"
    print(query)

    dfColumns = ['Time', 'User', 'Tweet ID', 'Tweet FULL']

    tw_df =[]
    tw_raw = tweetAPI(query)
    tw_df = tweetDF(tw_raw)


    today_date = now_datetime()
    print(today_date)
    filename = "%s-%s.%s" % (word_qry, today_date ,"csv")

    tw_df.to_csv(filename) 


    print("Fin de proceso")