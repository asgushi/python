import sys, csv, tweepy

#tokens
consumer_key="1NErWCeVRAQocB5OM7MzyvKi7"
consumer_secret="TNhfsPH2sbg8pQaoYStLuMCoiWKJZcMSm2bUSQSBQoa8JuDdES"
access_key = "39637886-hyt2Eg69Tr2dtC55spNlUBdLm7u3e2adXx7a1k1Xj"
access_secret = "MYOKFTFR3Pj6XnwxcBMUT8AWeGDWTpEDcwerlD68Eijtb"

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
