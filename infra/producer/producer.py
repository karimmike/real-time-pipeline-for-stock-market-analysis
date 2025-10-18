import time 
import json 
import requests 
from kafka import KafkaProducer
#import logging, sys
#logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


#INITIALIZE VARIABLES FOR API
API_key = "d3fpnu1r01qolkneaj4gd3fpnu1r01qolkneaj50"
# the real API endpoints
BASE_URL = "https://finnhub.io/api/v1/quote"
SYMBOLS = ["AAPL", "MSFT", "TSLA", "GOOGL", "AMZN"]
#forex_symbols = ["OANDA"]

#INITIALIZE PRODUCER
# creating the “data sender” (think of it like opening a pipeline 
# connection where we can push messages into Kafka)
producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)


#RETRIEVE DATA
#def fetch_forecexchange()

def fetch_quote(symbol):
    #Build the url, https://finnhub.io/api/v1/<endpoint>?<parameters>&token=YOUR_KEY
    url = f"{BASE_URL}?symbol={symbol}&token={API_key}"
    try: 
        # make the request
        response = requests.get(url)
        # check for errors
        response.raise_for_status()
        # change to json
        data = response.json()
        # add the data symbol and fetched-at
        data['symbol'] = symbol
        data['fetched_at'] = int(time.time()) # UTC time universal present time
        return data 
    except Exception as e:
        print(f"Error fetching {symbol}: {e}")
        return None
    
# Function might return siomething like that if we pass it AAPL 
# {  "c": 175.35,       # current price
#   "h": 176.00,        # high price of the day
#   "l": 174.50,        # low price of the day
#   "o": 175.00,        # open price of the day
#   "pc": 174.00,       # previous close
#   "symbol": "AAPL",   # added manually by the function
#   "fetched_at": 1696356000  # time you pulled this data
# }


# Iterate infinitely untill something happen
#LOOPING AND PUSH9ING TO STREAMIING
while True:
    for symbol in SYMBOLS:
        quote = fetch_quote(symbol)
        if quote:
            print(f"Producing: {quote}")
            producer.send("stock-quotes", value = quote)
    time.sleep(6)