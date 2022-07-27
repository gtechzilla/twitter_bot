import tweepy
import os
from dotenv import load_dotenv
load_dotenv()

from services import tweepy_auth,retweet_favourites

API_KEY = os.getenv('api_key')
API_SECRET = os.getenv('api_key_secret')
ACCESS_TOKEN = os.getenv('access_token')
ACCESS_TOKEN_SECRET = os.getenv('access_token_secret')

api = tweepy_auth(API_KEY,API_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
retweet_favourites(api,'okiomagerald')
