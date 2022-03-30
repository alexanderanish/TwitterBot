# importing the module
import tweepy

#import twitter credential
from credential import *


def deleteLastTweet(tweetId):
    # authentication of consumer key and secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # authentication of access token and secret
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    #delete tweet
    api.destroy_status(tweetId)