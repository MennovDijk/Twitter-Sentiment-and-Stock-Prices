import pandas as pd
from scipy.stats.morestats import wilcoxon

amt_lags = 48
file = 'Own_Classifier'
tweet_stock = 'polarity'

for lag in range(0,amt_lags+1):
    list_correlations = []
    for f in range(2,55):
        try:
            df = pd.read_excel('../thesis_files/Correlations_4_hour_lag/' + \
                               file + str(f) +'_laggedcorrelations_' + tweet_stock + '.xlsx')
            list_correlations.append(df['SP500 lagged correlations'][lag])
        except:
            continue
    print(file, tweet_stock, lag * 5, wilcoxon(list_correlations))


# for every lag, look at all the files and append all of the correlations for every lag to a list
# create a list of 0's with len(list_from_above), then wilcoxon(list(correlations), list(zeros) for each lag