# Modifikasi tampilan data
import pandas as pd
pd.set_option("display.max_columns",50)

table = pd.read_csv("D:/Pelatihan/DQLab/Python/penduduk_gender_head.csv")
table.head()
print(table)
