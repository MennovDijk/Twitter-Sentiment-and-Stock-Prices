import os
import pandas as pd

file = 'Textblob'
tweet_polarity = 'tweet'

lags = ['150', '185', '215', '220']

df = pd.read_excel('../thesis_files/Correlations_4_hour_lag/Combined_Data/Correlation Overview Graphing ' \
                   + file + ' ' +  tweet_polarity + '.xlsx')

for l in lags:
    above_zero = 0
    below_zero = 0
    for i in range(0, len(df['40'])):
        if df[l][i] > 0:
            above_zero += 1
        if df[l][i] < 0:
            below_zero += 1
    print(l, above_zero, below_zero)