from textblob import TextBlob
from nltk.corpus import twitter_samples
import numpy as np
import _pickle as CP

negative_file = twitter_samples.strings("negative_tweets.json")
trainer = [(x, 'neg') for x in negative_file[4000:5000]]
positive_file = twitter_samples.strings("positive_tweets.json")
trainer.extend([(x, 'pos') for x in positive_file[4000:5000]])

correct = 0
total = 0



def analyse_tweet(text):
    if TextBlob(text).sentiment[0] > 0.35 and TextBlob(text).sentiment[1] > 0.2:
        pos_neg = 'pos'
    elif TextBlob(text).sentiment[0] < 0.35 and TextBlob(text).sentiment[1] > 0.2:
        pos_neg = 'neg'
    else:
        pos_neg = 'neut'
    return pos_neg

for x in trainer:
    if analyse_tweet(x[0]) == x[1]:
            correct += 1
    total += 1



print("Accuracy score for the pre-trained TextBlob classifier", str(correct/total * 100)+'%' )



