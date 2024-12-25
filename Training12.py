# For example
import pandas as pd
data_visualization=pd.read_csv('penduduk_gender_head.csv')
data_visualization
# If we want to take the first 5 rows, use this: data_visualization.head()
# If we want to take the last 5 rows, use this: data_visualization.tail()
# if we want to know total row: len(data_visualization)

# How many unique data in dataset column?
data_visualization['NAMA KECAMATAN'].unique()

# We want to separate each unique data as unique dataframe, for example, just take dino, away, and star data
senen=data_visualization['NAMA KECAMATAN']== "SENEN"
senens=data_visualization[senen]
tanahabang=data_visualization["NAMA KECAMATAN"]=="TANAH ABANG"
tanahabangs=data_visualization[tanahabang]
menteng=data_visualization["NAMA KECAMATAN"]=="MENTENG"
mentengs=data_visualization[menteng]
senens.head()