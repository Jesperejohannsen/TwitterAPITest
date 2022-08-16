import tweepy
import time


auth = tweepy.OAuth1UserHandler("6KThT36MhNbjNUt1EnrWCe6ko",
                                "7mm2LjSY8KNThKMYmKjPGvDrvwipdlYHcYr729zNXBlwH6heXE",
                                "1559433882717634560-4qkq9bLcStuGmSgXYFKLI1UsTtsFfz",
                                "4yrgg0pyrqwU2q98bd30WyvkjxaE682cgaYW3lfyQin2s"
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


