from nltk.corpus import twitter_samples
import _pickle as CP

negative_file = twitter_samples.strings("negative_tweets.json")
trainer = [(x, 'neg') for x in negative_file[4000:5000]]
positive_file = twitter_samples.strings("positive_tweets.json")
trainer.extend([(x, 'pos') for x in positive_file[4000:5000]])

correct = 0
total = 0

with open('my_dumped_classifier.pkl', 'rb') as f:
    cl = CP.load(f)
f.close()

print(cl.accuracy(trainer))


print("Accuracy score for Naïve Bayes Classifier as trained by authors of the paper:", correct/total)



