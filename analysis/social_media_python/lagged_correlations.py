import pandas as pd
import numpy as np
import os

os.chdir('C:/Users/ikdem/PycharmProjects/Thesis_Analysis/Social_Media_Files')

companies = ['aNike Stock', 'bSteven Madden Stock', 'cSketchers Stock', 'dWolverine World Wide Stock']

#set number of lags
amt_lags = 48

#for all files to analyze
for f in range(0,30):
    df = pd.read_excel('SMA_Classifier'+str(f)+'.xlsx')
    df2 = pd.DataFrame()
    for c in companies:
        lags = []
        # for the lags set previously
        for lag in range(0,amt_lags+1):
            l1 = []
            l2 = []
            # for the length of the stock price
            for i in range(0, len(df[c])):
                # if there is a stock price change (markets are open) and the lag is not non-existent, append the polarity measure and stock price to a list
                if str(df[c][i]) != '0.0' and i-lag > 0:
                    l2.append(float(df[c][i]))
                    # l1.append(float(df['numTweets Normalized'][i-lag]))
                    l1.append(float(df['Polarity Normalized'][i-lag]))
            # calculate the correlation PER LAG and append it to a seperate list
            corr = np.corrcoef(l1, l2)[0, 1]

            lags.append(float(corr))
        # save everything to a seperate excel file that just contains the lags of the corresponding files.
        df2[c+' lagged correlations'] = lags
        df2.to_excel('file' + str(f) + '_laggedcorrelationspolarity.xlsx', sheet_name='sheet1', index=False)


