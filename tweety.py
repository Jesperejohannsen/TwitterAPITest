import tweepy
import time


auth = tweepy.OAuth1UserHandler("API Key here",
                                "API Key Secret here",
                                "Access Token here",
                                "Access Token Secret here"
                                )


api = tweepy.API(auth)
user = api.me()


def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


search_string = "python"
numbersOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
    try:
        tweet.favorite()
        print("I liked that tweet!")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


