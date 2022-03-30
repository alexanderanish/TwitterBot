# importing the module
import tweepy

#import twitter credential 
from credential import *


def getLatestTweet(username, content):
    # authentication of consumer key and secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # authentication of access token and secret
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    
    # fetching the statuses
    statuses = api.user_timeline(screen_name=username)


    # By default api.user_timeline() gets the last 20 tweets, but you can specify it
    # with the count parameter
    #tweet= statuses[0] # An object of class Status (tweepy.models.Status)
    #return(tweet.id)# Print ID of tweet
    #list of tweet IDs
    tweetListId=[]

    #Loop to find relevant tweet 
    for tweet in statuses:
        if content in tweet.text:
            tweetListId.append(tweet.id)
            
    return(tweetListId)


