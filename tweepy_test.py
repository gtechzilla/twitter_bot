import tweepy
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('api_key')
api_secret = os.getenv('api_key_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')


auth = tweepy.OAuthHandler(api_key,api_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

#returns the tweets liked by a given user
tweet_list = api.favorites(screen_name='okiomagerald')
for tweet in tweet_list:
    # Retweet a tweet based on id
    try:
        api.retweet(tweet.id)
    except tweepy.TweepError as e:
        print(e)