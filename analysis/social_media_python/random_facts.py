import pandas as pd
import numpy as np
import os

companies = ['aNike Stock Normalized', 'bSteven Madden Stock Normalized', 'cSketchers Stock Normalized', 'dWolverine World Wide Stock Normalized']

os.chdir('C:/Users/ikdem/PycharmProjects/Thesis_Analysis/Social_Media_Files')

total_tweets = []
greatest_stock_change = 0
greatest_polarity_change = 0

for f in range(0,31):
    df = pd.read_excel('SMA_Classifier'+str(f)+'.xlsx')
    for i in range(0,len(df['fTotal Tweets Counted'])):
        if df['Polarity Normalized'][i] < greatest_polarity_change:
            greatest_polarity_change = df['Polarity Normalized'][i]
            time_polarity = df['gTime of Tweets'][i]
        for c in companies:
            if df[c][i] < greatest_stock_change:
                greatest_stock_change = df[c][i]
                company = c
                time_stock = df['gTime of Tweets'][i]
        total_tweets.append(df['fTotal Tweets Counted'][i])

print(sum(total_tweets), sum(total_tweets) / 30)
print(greatest_polarity_change, time_polarity)
print(greatest_stock_change, company, time_stock)