from textblob import TextBlob
import tweepy
import csv

consumer_api = '' #Your consumer api
consumer_api_secret = '' #Your consumer api secret

access_token = '' #Your access token
access_token_secret = '' #Your access token secret

auth = tweepy.OAuthHandler(consumer_api, consumer_api_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

tweets = api.search('intelligence')

with open('tweet_this.csv', 'w') as tweet_file:
	twitter = csv.writer(tweet_file)
	for tweet in tweets:
		twitter.writerow(tweet.text.encode('utf-8'))
		wiki = TextBlob(tweet.text)
		print(wiki.sentiment.polarity)
