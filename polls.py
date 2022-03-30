#curl -X POST https://api.twitter.com/2/tweets -H "Authorization: Bearer AAAAAAAAAAAAAAAAAAAAACvOYAEAAAAAgs%2FFQBDTos0SopkeGFpQ5oUoLzg%3DHdCSySr8B0fLQ8ah4UtjpZNyhQnZrz9wDOjcpTWnbp9lLIQrWa" -H "Content-type: application/json" -d '{"text": "Are you excited for the weekend?", "poll": {"options": ["yes", "maybe", "no"], "duration_minutes": 120}}'''
#resp = requests.post(url, json=data, params=params, auth=OAuth1(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET))
import json
import requests

from requests_oauthlib import OAuth1

from credential import *
from db import get_database




def connect_to_endpoint(url, data, params=None ):
    resp=None
    resp=requests.post(url, json=data, params=params, auth=OAuth1(consumer_key, consumer_secret, access_token, access_token_secret))

    if not resp.status_code in (200, 201):
        raise Exception(resp.status_code, resp.text)
    return resp.json()

    



def create_poll(data):
    ''' Creates a Twitter poll using the given question and options '''
    options=["Bearish", "Neutral", "Bullish"]
    #print(len(data["ticker"]))
    datalen=len(data["ticker"])
    ticker= data["ticker"]

    #for logging
    # Get the database
    Polls = get_database()

    #print(dbname)

    TweetLogs= Polls["TweetLogs"]

    for i in range(datalen):
        stock=str(ticker[i])
    
        url = 'https://api.twitter.com/2/tweets'
        data = {
            'text': f'What are your sentmiments on ${stock}? #{stock} #wallstreetbets #StockWatch #WallStreetMooners',
            'poll': {
                'options': options,
                'duration_minutes': 24 * 60
            }
        }
        
        res=connect_to_endpoint(url, data=data)
        logData = {
            'text': f'What are your sentmiments on ${stock}? #{stock} #wallstreetbets #StockWatch #WallStreetMooners',
            'poll': {
                'options': options,
                'duration_minutes': 24 * 60
            },
            'tweetResponse': res
        }
        TweetLogs.insert_one(logData)
        #print(res)

    print("Done Tweeting!")
   

if __name__ == '__main__':
    question="What are your sentiments on Tesla ($TSLA)?"
    options=["Bearish", "Neutral", "Bullish"]
    create_poll(question, options)
