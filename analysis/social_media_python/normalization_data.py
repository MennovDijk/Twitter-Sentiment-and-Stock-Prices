import pandas as pd
import os

def normalize_data(l):
    nl = []
    for i in range(1,len(l)):
        nl.append(((l[i]-l[i-1])/l[i-1]))
    nl.append(0)
    return nl

os.chdir('C:/Users/ikdem/PycharmProjects/Thesis_Analysis/Social_Media_Files')

file = 'SMA_Classifier'

companies = ['aNike Stock', 'bSteven Madden Stock', 'cSketchers Stock', 'dWolverine World Wide Stock']


for i in range(0,29+1):
    print('Working on file:', i)
    for c in companies:
        print('Working on company:', c)
        df = pd.read_excel(file+str(i)+'.xlsx')
        pos_neg_list = normalize_data(df['ePos/Neg Sentiment'].tolist())
        df['Polarity Normalized'] = pos_neg_list
        num_tweets_list = normalize_data(df['fTotal Tweets Counted'].tolist())
        df['numTweets Normalized'] = num_tweets_list
        stock_list = normalize_data(df[c].tolist())
        df[c+' Normalized'] = stock_list
        df.to_excel(file+str(i)+'.xlsx', index=False)
        print('done...')


