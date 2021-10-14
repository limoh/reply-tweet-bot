import tweepy
#import keys from tkens file
from tkens import tkens

CONSUMER_KEY = tkens['consumer_key']
CONSUMER_SECRET = tkens['consumer_secret']
ACCESS_TOKEN = tkens['access_token']
ACCESS_TOKEN_SECRET = tkens['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

twts = api.search(q="Hello World!")

#list of specific strings we want to check for in Tweets
t = ['Homework',
     'Essay help',
     'Assignment due',
    ]

for s in twt:
    for i in t:
        if i == s.text:
            sn = s.user.screen_name
            m = "@%s Hello, I can help you with your homework" % (sn)
            s = api.update_status(m, s.id)