import os
import pandas as pd


for i in range(32,54):
    df = pd.read_excel('../thesis_files/Correlations_4_hour_lag/Textblob' \
                       + str(i) + '_laggedcorrelations_polarity' + '.xlsx')

    df.to_excel('../thesis_files/Correlations_4_hour_lag/Textblob' \
                + str(i-1) + '_laggedcorrelations_polarity' + '.xlsx', index=False)