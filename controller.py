#import latestTweet module
##from latestTweet import getLatestTweet

#import delete tweet module
##from deleteTweet import deleteLastTweet

#import post tweet module
##from tweet import tweet

import datetime

from pandas import DataFrame

import csv

from polls import create_poll

from marketCap import marketCap

from db import get_database




#tweet to delete
##tweetText="Video here:"

#text to tweet
##tweetInput="""The best stock & crypto sentiment. Join Wall Street Mooners! Video here: 
##http://youtu.be/tJt-1H6apd8

##http://wallstreetmooners.com

##$AAPL $AMZN $NVDA $NIO $TSLA $GME $AMC  #cryptocurrecy #Stocks $BTC $ETH .xyz"""

#account to tweet from
##username="antalexaa"

#fetch latest tweet and delete
##print("finding last tweet")

#extrating last matching tweet
##Ids=getLatestTweet(username, tweetText)

##print("deleting last tweet")

##deleteLastTweet(Ids[0])

##print("posting new tweet")

#post latest tweet

##tweet(tweetInput)

##print("successfully posted new tweet")
def getTodayTweets():

    tday = datetime.datetime.now()

    numTday = int(tday.strftime("%w"))

    # Get the database
    Polls = get_database()

    #print(dbname)

    StockData= Polls["StockData"]

    dataToTweet=StockData.find({"tweetDay":numTday},{"_id":0, "ticker": 1})

    items_df = DataFrame(dataToTweet)

    return items_df.to_dict()

def getListFromFile(filename='Stock_Poll_List.csv'):

    with open(filename) as file:
        content = file.readlines()
    rows = content[1:]

    tickerList=[]
    for i in rows:
        tickerList.append(str(i).strip())
    return tickerList


def insertTickerDB(data):
    # Get the database
    Polls = get_database()

    #print(dbname)

    StockData= Polls["StockData"]

    dbData=[]

    sizeOfData= len(data)
    perday = int(sizeOfData/5)+1

    counter = 1
    weekday = 1

    for i in data:

        if counter < perday:
            counter +=1

            dbData.append( {

            "ticker" : str(i),
            "marketCap" : data[i],
            "Order" : 0,
            "tweetDay":weekday
            })
        elif counter == perday:
            counter = 1
            dbData.append( {

            "ticker" : str(i),
            "marketCap" : data[i],
            "Order" : 0,
            "tweetDay":weekday
            })
            weekday += 1

    print("create insert list")

    #print(dbData)

    StockData.insert_many(dbData)

    print("inserted into db")

#print(tickerList)

#data=getListFromFile()

#tickerCap = marketCap(data)

#insertTickerDB(tickerCap)

create_poll(getTodayTweets())






