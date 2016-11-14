# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Variables that contains the user credentials to access Twitter API
access_token = "430059619-nrssaangYYQ2P6FwhhFpCPghyoPvN2Gho9fRqsqB"
access_token_secret = "RNH2Z8qQBZuGQz6zFxOGUpaLq5hiLSKY8bVYgzHf7IPHl"
consumer_key = "n2KGqpqYeYHkX53B5VCnTMuVa"
consumer_secret = "YAY0MeTzbg4z5qCLEWj8GYu7pqWldiReE3aTwAqnj6AbIrY99j"


# This is a basic listener that just prints received tweets to stdout.


class StdOutListener(StreamListener):
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    # This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python'])
