import os
import pandas as pd

os.chdir('C:/Users/ikdem/PycharmProjects/Thesis_Analysis/Thesis_Files')

for f in range(8,54):
    df = pd.read_excel('Own_Classifier' + str(f) + '.xlsx')
    for r in range(0,len(df['Time'])):
        if '2017-05-08' in str(df['Time'][r]):
            print(f)