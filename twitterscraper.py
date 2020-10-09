import sys
import re
import urllib2
import time

#http://www.tweepy.org/
import tweepy

#Get your Twitter API credentials and enter them here
consumer_key = "7ZOCRSoDj7s98J1rIoKNEfaC8"
consumer_secret_key = "VpuPG2kLwF9b63ryupu3lLrcS01Wi3IDfsZLX7xNdv0HVwLvzC"
access_key = ""
access_secret = ""

#method to get a user's last 200 tweets
def get_tweets(username):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

#set count to for number of links you want
    number_of_links = 1000

#get tweets for links
    tweets = api.user_timeline(screen_name = username,count = number_of_links)
#get urls for tweets
    for tweet in tweets:
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet.text)
        for url in urls:
            print url 

#if we're running this as a script
if __name__ == '__main__':

#get tweets for username passed at command line
    if len(sys.argv) == 2:
        get_tweets(sys.argv[1])
    else:
        print "Error: enter one username"