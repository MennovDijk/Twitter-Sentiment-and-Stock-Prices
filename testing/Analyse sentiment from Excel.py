import pandas as pd
from textblob import TextBlob
import os
import numpy


os.chdir('C:/Users/ikdem/Dropbox/School/Year 3/Bachelor thesis/Excel Outputs')

file = input('What Excel file to analyze?')

def normalize_data(l):
    nl = []
    for i in range(1,len(l)):
        nl.append(((l[i]-l[i-1])/l[i-1]))
    nl.append(0)
    return nl


for i in range(12,15+1):
    df = pd.read_excel(file+str(i)+'.xlsx')
    pos_neg_list = normalize_data(df['Pos/Neg Sentiment'].tolist())
    df['Polarity Normalized'] = pos_neg_list
    stock_list = normalize_data(df['Stock Price'].tolist())
    df['Stock Price Normalized'] = stock_list
    df.to_excel(file+str(i)+'.xlsx', index=False)







