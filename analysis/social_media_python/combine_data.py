import pandas as pd
import numpy as np
import os

amt_lags = 12

os.chdir('C:/Users/ikdem/PycharmProjects/Thesis_Analysis/Social_Media_Files')
df = pd.DataFrame()
df['''Amount of lag (* 5 minutes)'''] = [i for i in range(0,amt_lags+1)]

companies = ['aNike Stock lagged correlations', 'bSteven Madden Stock lagged correlations', 'cSketchers Stock lagged correlations', 'dWolverine World Wide Stock lagged correlations']

NikeAverage = []
NikeSTD = []

StevenAverage = []
StevenSTD = []

SketchersAverage = []
SketchersSTD = []

WolverineAverage = []
WolverineSTD = []


for lag in range(0,amt_lags+1):
    lNike = []
    lSteven = []
    lSketchers = []
    lWolverine = []
    for f in range(0, 30):
        cdf = pd.read_excel('file' + str(f) + '_laggedcorrelationspolarity' + '.xlsx')
        for c in companies:
            if c == 'aNike Stock lagged correlations':
                lNike.append(float(cdf[c][lag]))
            if c == 'bSteven Madden Stock lagged correlations':
                lSteven.append(float(cdf[c][lag]))
            if c == 'cSketchers Stock lagged correlations':
                lSketchers.append(float(cdf[c][lag]))
            if c == 'dWolverine World Wide Stock lagged correlations':
                lWolverine.append(float(cdf[c][lag]))


    NikeAverage.append(sum(lNike) / float(len(lNike)))
    NikeSTD.append(np.std(lNike, ddof = 1))

    SketchersAverage.append(sum(lSketchers) / float(len(lSketchers)))
    SketchersSTD.append(np.std(lSketchers, ddof=1))

    WolverineAverage.append(sum(lWolverine) / float(len(lWolverine)))
    WolverineSTD.append(np.std(lWolverine, ddof=1))

    StevenAverage.append(sum(lSteven) / float(len(lSteven)))
    StevenSTD.append(np.std(lSteven, ddof=1))

df['bNike Correlation'] = NikeAverage
df['bNike STD'] = NikeSTD

df['cSketchers Correlation'] = SketchersAverage
df['cNike STD'] = SketchersSTD

df['dWolverine Correlation'] = WolverineAverage
df['dWolverine STD'] = WolverineSTD

df['eSteven Correlation'] = StevenAverage
df['eSteven STD'] = StevenSTD

df.to_excel('Correlation Overview Polarity.xlsx', sheet_name='sheet1', index=False)








# for each file, and then for each stock get the average of correlations for each individual lag and also get the standard deviation
# this should give the same output as laggedcorrelation files only then with average AND standard deviation next to average
# 0.0355419559298335