from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
from apscheduler.schedulers.background import BackgroundScheduler
import json, time, googlefinance, re, sys, datetime
import pandas as pd

interval = float(input('Interval to store/print data? (minutes)'))
run_time = float(input('Time to run the program? (hours)'))

# obtain app from https://apps.twitter.com/ and fill in the information below:
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

printScheduler = BackgroundScheduler()


def analyse_tweet_textblob_classifier(text):
    if TextBlob(text).sentiment[0] > 0 and TextBlob(text).sentiment[1] > 0.3:
        pos_neg = 'pos'
    elif TextBlob(text).sentiment[0] < 0 and TextBlob(text).sentiment[1] > 0.3:
        pos_neg = 'neg'
    else:
        pos_neg = 'neut'
    return pos_neg


def get_stock_price(stock):
    data = json.loads(json.dumps(googlefinance.getQuotes(stock)))
    return data[0].get('LastTradePrice').replace(',','')

timeStop = time.time() + 60*60*run_time

class StdOutListener(StreamListener):
    def __init__(self):
        self.posCount = 1
        self.negCount = 1
        self.tweetsCounted = []
        self.NikeData = []
        self.SketchersData = []
        self.WolverineData = []
        self.StevenData = []
        self.tweetData = []
        self.timeData = []

    def on_data(self, data):
        data = json.loads(data)
        if time.time() < timeStop:
            try:
                if 'rt' not in data['text'].lower() and data['user']['followers_count'] > 50 and data['user'][
                    'lang'] == 'en' and 'youtube' not in data['text'].lower():
                    result = re.sub(r"http\S+", "", data['text'])
                    print(result, analyse_tweet_textblob_classifier(result))
                    if analyse_tweet_textblob_classifier(result) == 'pos':
                        self.posCount += 1
                        self.tweetsCounted += 1
                    if analyse_tweet_textblob_classifier(result) == 'neg':
                        self.negCount += 1
                        self.tweetsCounted += 1
            except:
                pass
            return True
        else:
            printScheduler.shutdown()
            return


    def on_error(self, status):
        print(status)

    def returns_data(self):
        return self.NikeData, self.StevenData, self.SketchersData, self.WolverineData, self.tweetData, self.tweetsCounted, self.timeData

    def reset(self):
        self.wordsCounted = 0
        self.negCount = 1
        self.posCount = 1

    def prints_data(self):
        print(self.posCount, self.negCount)
        self.NikeData.append(float(get_stock_price('NYSE:NKE')))
        self.StevenData.append(float(get_stock_price('NASDAQ:SHOO')))
        self.SketchersData.append(float(get_stock_price('NYSE:SKX')))
        self.WolverineData.append(float(get_stock_price('NYSE:WWW')))
        self.tweetData.append(float(self.posCount/self.negCount))
        self.tweetsCounted.append(int(self.posCount + self.negCount))
        self.timeData.append(str(datetime.datetime.now()))
        self.reset()


if __name__ == '__main__':

    #This handles Twitter authentification and the connection to Twitter Streaming API
    l = StdOutListener()
    printScheduler.add_job( l.prints_data, 'interval', seconds=(60*interval) )
    printScheduler.start()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    while time.time() < timeStop:
        time.sleep(1)
        try:
            stream = Stream(auth, l)
            stream.filter(track=['shoes', 'shoe', 'sneakers', 'sneaker', 'boot', 'boots'], stall_warnings=True)
        except:
            e = sys.exc_info()[0]
            print('error', e)


df = pd.DataFrame({'aNike Stock': l.returns_data()[0], 'bSteven Madden Stock': l.returns_data()[1], 'cSketchers Stock': l.returns_data()[2], 'dWolverine World Wide Stock': l.returns_data()[3], 'ePos/Neg Sentiment': l.returns_data()[4], 'fTotal Tweets Counted': l.returns_data()[5], 'gTime of Tweets': l.returns_data()[6]})

df.to_excel('SMA_Classifier.xlsx', sheet_name='sheet1', index=False)

print('done')

