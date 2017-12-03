from textblob import TextBlob
import tweepy

consumer_api = '' #Your consumer api
consumer_api_secret = '' #Your consumer api secret

access_token = '' #Your access token
access_token_secret = '' #Your access token secret

auth = tweepy.OAuthHandler(consumer_api, consumer_api_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

tweets = api.search('intelligence')

for tweet in tweets:
	print(tweet.text)
	wiki = TextBlob(tweet.text)
	print(wiki.sentiment.polarity)
