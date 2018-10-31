from nltk.corpus import twitter_samples
from textblob import classifiers
import _pickle as cPickle
import time


negative_file = twitter_samples.strings("negative_tweets.json")
trainer = [(x, 'neg') for x in negative_file[:2500]]
print('done')
positive_file = twitter_samples.strings("positive_tweets.json")
trainer.extend([(x, 'pos') for x in positive_file[:2500]])
print('done')

t1 = time.time()
cl = classifiers.NaiveBayesClassifier(trainer)
print(time.time() - t1)

with open('classifier.pkl', 'wb') as f:
    cPickle.dump(cl, f)
f.close()

