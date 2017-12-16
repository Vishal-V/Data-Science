from textblob import TextBlob
import tweepy
import csv

consumer_api = 'iyQlW0cR7IQeEG3stLDndIkFv'
consumer_api_secret = 'X4ZMHB87834N9ndE9gZ7gX0wUn8JuwVzhfKZFYRY7vpCwlr2Xu'

access_token = '937370951510982657-aIMAP51uiNa4bvn9tSLsjxOkNF5n4fU'
access_token_secret = 'BznTSpZwtgmgvzFFhSnyNkxck9IlySz4Xjx8zi8V2ioEx'

auth = tweepy.OAuthHandler(consumer_api, consumer_api_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

tweets = api.search('happy')

with open('tweet_this.csv', 'w') as tweet_file:
	twitterit = csv.writer(tweet_file)
	for tweet in tweets:
		twitterit.writerow(tweet.text.encode('utf-8'))
		wiki = TextBlob(tweet.text)
		print(wiki.sentiment)