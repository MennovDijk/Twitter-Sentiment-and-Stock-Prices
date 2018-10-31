import pandas as pd
import numpy as np
import os

amt_lags = 12
amt_files = 29
os.chdir('C:/Users/ikdem/PycharmProjects/Thesis_Analysis/Social_Media_Files')
df = pd.DataFrame()
df['File number'] = [i for i in range(0,amt_files+1)]

companies = ['aNike Stock lagged correlations', 'bSteven Madden Stock lagged correlations', 'cSketchers Stock lagged correlations', 'dWolverine World Wide Stock lagged correlations']

for lag in range(0,amt_lags+1):
    for c in companies:
        company_correlation = []
        for f in range(0,amt_files+1):
            cdf = pd.read_excel('file' + str(f) + '_laggedcorrelationspolarity.xlsx')
            company_correlation.append(cdf[c][lag])
        df[c + ' numlag: ' + str(lag)] = company_correlation


df.to_excel('Correlation Overview Graphing Polarity.xlsx', sheet_name='sheet1', index=False)
# for each lag, check all of the files and append them to a list
# then