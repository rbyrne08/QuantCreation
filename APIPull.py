import requests
import time
import pandas as pd
from config import client_id
import plotly.graph_objects as go

#The daily prices endpoints
def pricehistory():
    #Define endpoint
    endpoint = r"https://api.tdameritrade.com/v1/marketdata/{}/pricehistory".format('AMD')

    #Define payload
    payload = {'apikey':client_id,
               'periodType': 'day',
               'frequencyType':'minute',
               'frequency':'1',
               'period':'2',
               'endDate':int(time.time()*1000),
               'startDate':int(time.mktime((2020,1,1,0,0,0,0,0,0))*1000),
               'needExtendedHours':'true'
               }

    #make a request
    content = requests.get(url=endpoint,params=payload)

    data = content.json()

    dataframe = pd.DataFrame.from_dict(data.get("candles"))
    dataframe['date'] = pd.to_datetime(dataframe['datetime'],unit='ms')
    print(dataframe)
    fig = go.Figure(data=[go.Candlestick(x=dataframe['date'],
                                         open=dataframe['open'],
                                         high=dataframe['high'],
                                         low=dataframe['low'],
                                         close=dataframe['close'])])

    fig.show()



def getQuote():
    #Define endpoint
    endpoint = r"https://api.tdameritrade.com/v1/marketdata/{}/quotes".format('AMD')

    #Define payload
    payload = {'apikey':client_id}

    #make a request
    content = requests.get(url=endpoint,params=payload)

    data = content.json()

    print(data)

pricehistory()