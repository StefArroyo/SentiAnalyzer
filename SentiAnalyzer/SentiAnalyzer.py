import configparser
import json
import requests
import os

CONFIG_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', "config.ini"))

config = configparser.ConfigParser()
config.read(CONFIG_FILE)
API_KEY = config['DEFAULT']['API_KEY']
API_ENDPOINT = config['DEFAULT']['API_ENDPOINT']
HEADERS = {'Ocp-Apim-Subscription-Key': f"{API_KEY}"}

def get_sentiment(sentiment_data) :
    api_url_sentiment = f"{API_ENDPOINT}sentiment"
    return http_post_request(api_url_sentiment, sentiment_data)
    
def http_post_request(api_url, sentiment_data):
    return requests.post(api_url, headers=HEADERS, json=sentiment_data)



if __name__ == "__main__" : 
    documents = {'documents':[{'id': '1', 'text': 'This product is awesome!'}]}
    response = get_sentiment(documents)
    print(response.json())
