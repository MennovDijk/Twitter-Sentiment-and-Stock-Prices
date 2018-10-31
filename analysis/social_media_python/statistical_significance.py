import pandas as pd
import numpy as np
from scipy.stats.morestats import wilcoxon
import os
import matplotlib.pyplot as plt

os.chdir('C:/Users/ikdem/PycharmProjects/Thesis_Analysis/Social_Media_Files')

amt_lags = 12

tweet_polarity = 'polarity'

companies = ['aNike Stock lagged correlations', 'bSteven Madden Stock lagged correlations', 'cSketchers Stock lagged correlations', 'dWolverine World Wide Stock lagged correlations']

for c in companies:
    for lag in range(0,amt_lags+1):
        list_correlations = []
        for f in range(0,30):
            try:
                df = pd.read_excel('file' + str(f) +'_laggedcorrelations' + tweet_polarity + '.xlsx')
                list_correlations.append(df[c][lag])
            except:
                continue
        print(str(f), c, tweet_polarity, lag * 5, wilcoxon(list_correlations))


# for every lag, look at all the files and append all of the correlations for every lag to a list
# create a list of 0's with len(list_from_above), then wilcoxon(list(correlations), list(zeros) for each lag