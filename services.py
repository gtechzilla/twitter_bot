import tweepy_test

def tweepy_auth(api_key,api_secret,access_token,access_token_secret):
    """
    Authenticates us with the twitter api
    """
    auth = tweepy.OAuthHandler(api_key,api_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)

    return api

def retweet_favourites(api,username):
    """
    retweets liked tweets of a given user account
    """
    #returns the tweets liked by a given user
    tweet_list = api.favorites(screen_name=username)
    for tweet in tweet_list:
        # Retweet a tweet based on id
        try:
            api.retweet(tweet.id)
        except tweepy.TweepError as e:
            print(e)