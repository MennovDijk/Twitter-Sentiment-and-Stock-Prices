import pandas as pd
import os

df = pd.DataFrame()

df['''Amount of lag'''] = [i * 5 for i in range(0,49)]

file = 'Textblob'
tweet_polarity = 'tweet'

list_average_final = []


for lag in range(0,49):
    list_intermediate_correlations = []
    list_intermediate_dates = []
    for f in range(1, 54):
        try:
            cdf = pd.read_excel('../thesis_files/Correlations_4_hour_lag/' \
                                + file + str(f) + '_laggedcorrelations_'+ tweet_polarity + '.xlsx')

            list_intermediate_correlations.append(cdf['SP500 lagged correlations'][lag])
        except:
            continue
    list_average_final.append(sum(list_intermediate_correlations)/float(len(list_intermediate_correlations)))


df['Stock Average correlation'] = list_average_final

df.to_excel('../thesis_files/Correlations_4_hour_lag/Combined_Data/Overview ' \
            + tweet_polarity + ' ' + file + '.xlsx', sheet_name='sheet1', index=False)








# for each file, and then for each stock get the average of correlations for each individual lag and also get the standard deviation
# this should give the same output as laggedcorrelation files only then with average AND standard deviation next to average
# 0.0355419559298335