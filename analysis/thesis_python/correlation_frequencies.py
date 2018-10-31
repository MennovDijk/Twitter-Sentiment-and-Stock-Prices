import os
import pandas as pd


os.chdir('C:/Users/ikdem/Dropbox/School/Year 3/Bachelor thesis/Thesis_Files/Correlations_4_hour_lag/Combined_Data/imhacky')

df = pd.read_excel('Correlation Overview Graphing Own_Classifier polarity test.xlsx')

def round_nearest(x):
    try:
        return round(x / 0.05) * 0.05
    except:
        return 0.05

i = 5

counts = dict()

while i < 240:
    new_list = []
    for n in range(0,len(df[str(i)])):
        new_list.append(round_nearest(df[str(i)][n]))
    for x in new_list:
        counts[x] = counts.get(x, 0) + 1
    i += 5

dfx = pd.DataFrame(counts, index=[0])
dfx.to_excel('frequencypolarityown.xlsx')


