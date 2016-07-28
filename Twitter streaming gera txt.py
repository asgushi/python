import sys, csv, tweepy

#tokens
consumer_key=""
consumer_secret=""
access_key = ""
access_secret = ""

#acessando twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#criando objeto 'customStreamListener'

class CustomStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        encoded = status.text.encode("utf-8", errors='ignore').lower().split()
        print(encoded)
        with open('tweets.txt', 'a', newline="") as f: 
            writer = csv.writer(f)
            writer.writerow([encoded])
            f.close()

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

streamingAPI = tweepy.streaming.Stream(auth, CustomStreamListener())
#filtro
#streamingAPI.filter(track=['ibovespa', 'investimento', 'investimentos', 'investir', 'bovespa', 'bmf', 'tesouro direto', 'finanças', 'bm&fbovespa', 'mercado de capitais'])
streamingAPI.filter(track=['brasil'])
