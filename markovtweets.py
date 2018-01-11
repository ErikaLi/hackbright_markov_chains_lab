import os

import twitter

api = twitter.Api(
    consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
    consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
    access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
    access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET']
)

#print api.VerifyCredentials()

#status = api.PostUpdate("Test")
#print status.text

def update(string):
    status = api.PostUpdate(string)
    print status.text