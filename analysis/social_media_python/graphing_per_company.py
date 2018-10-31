import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
amt_lags = 12
os.chdir('C:/Users/ikdem/PycharmProjects/Thesis_Analysis/Social_Media_Files')

companies = ['aNike Stock lagged correlations', 'bSteven Madden Stock lagged correlations', 'cSketchers Stock lagged correlations', 'dWolverine World Wide Stock lagged correlations']

df = pd.read_excel('Correlation Overview Graphing Polarity.xlsx')
nikedf = pd.DataFrame()
stevdf = pd.DataFrame()
sketdf = pd.DataFrame()
wolvdf= pd.DataFrame()

nikedf['File number'] = [i for i in range(0,30)]
stevdf['File number'] = [i for i in range(0,30)]
sketdf['File number'] = [i for i in range(0,30)]
wolvdf['File number'] = [i for i in range(0,30)]

for c in companies:
    outdf = pd.DataFrame()
    for lag in range(0,amt_lags+1):
        correl_list = []
        for l in range(0,30):
            correl_list.append(df[c + ' numlag: ' + str(lag)][l])
        if c == 'aNike Stock lagged correlations':
            nikedf[str(lag*5)] = correl_list
        if c == 'bSteven Madden Stock lagged correlations' :
            stevdf[str(lag*5)] = correl_list
        if c == 'cSketchers Stock lagged correlations':
            sketdf[str(lag*5)] = correl_list
        if c == 'dWolverine World Wide Stock lagged correlations':
            wolvdf[str(lag*5)] = correl_list


nikedf.to_excel('aNike graphing polarity.xlsx', sheet_name='sheet1', index=False)
stevdf.to_excel('aSteven Madden graphing polarity.xlsx', sheet_name='sheet1', index=False)
sketdf.to_excel('aSketchers graphing polarity.xlsx', sheet_name='sheet1', index=False)
wolvdf.to_excel('aWolverine graphing polarity.xlsx', sheet_name='sheet1', index=False)


