#Twitter Profiler app. This is a simple script to configure the Twitter API

import tweepy
import time #https://github.com/tweepy/tweepy

# Twitter API credentials. Get yours from apps.twitter.com. Twitter acct rquired
# If you need help, visit https://dev.twitter.com/oauth/overview
consumer_key = "cl881cIJOdvaBZjhGnARhLcVX"
consumer_secret = "IGmAcUxKVT8suHO0aVXkJpFw3toNhMZjl8vg4sOJdG3TiliddK"
access_key = "933368297965391873-99yKrrYXxzCRjD6t9bIDTUpw2xFcVni"
access_secret = "DUXiX1EwWKVf9uhYMhgxzlgofC70CaLHCInhgy31dxtEs"

# this function collects a twitter profile request and returns a Twitter object
def get_profile(screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    try:
        #https://dev.twitter.com/rest/reference/get/users/show describes get_user
        user_profile = api.get_user(screen_name)
    except:
        user_profile = "broken"

    return user_profile

# uses the function to query a Twitter user. Try s = get_profile("cd_conrad")
s = get_profile("CitronResearch")
print "Name: " + s.name
print "Location: " + s.location
print "Description: " + s.description
print "Id: " + s.id_str
