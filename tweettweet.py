import tweepy
import time

def print_public_tweets(api):
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)
    except StopIteration:
        print('That\'s all folks')

def follow_user(username):
    '''
    We wrap the Cursor with the limit_handler to pause when we hit the Twitter
    limit of pinging the server
    '''
    for follower in limit_handler(tweepy.Cursor(api.followers).items()):
        if follower.name == username:
            follower.follow()
            break

def like_numOfTweets_with_keyword(search_keyword, numberOfTweets):
    for tweet in limit_handler(tweepy.Cursor(api.search, search_keyword).items(numberOfTweets)):
        try 
            tweet.favorite()
            print('I liked that tweet')
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

auth = tweepy.OAuthHandler('l3v76oXmlBGAHf30b','XbSgzch72xUhwhsVPjtvOFurct78vs')
auth.set_access_token('E1ed2mxTgy0yaoHYUMThYeJ1', 'IwWxTXPdMb5KleYTgl')

api = tweepy.API(auth)
user = api.me()
username = 'ElonMusk'

print_public_tweets(api)
follow_user('username')

search_string = 'python'
numberOfTweets = 2

like_numOfTweets_with_keyword(search_string, numberOfTweets)
