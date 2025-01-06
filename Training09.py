# Viusualisi Data menjadi Bar Chart
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


table = pd.read_csv("D:/Pelatihan/DQLab/Python/penduduk_gender_head.csv")
table.head()
x_label = table['NAMA KELURAHAN']
plt.bar(x=np.arange(len(x_label)),height=table['LAKI-LAKI WNI'])
plt.xticks(np.arange(len(x_label)), table['NAMA KELURAHAN'], rotation=90)
plt.xlabel('Kelurahan di Jakarta Pusat')
plt.ylabel('Jumlah Penduduk Laki - Laki')
plt.title('Persebaran Jumlah Penduduk Laki- Laki di Jakarta Pusat')

plt.show()

# Penjelasan kode:
# 1. Mengimport library pandas sebagai pd, numpy sebagai np, dan matplotlib.pyplot sebagai plt.
# 2. Membaca file CSV yang berisi data penduduk gender di suatu kelurahan menggunakan fungsi pd.read_csv() dan menyimpannya ke dalam variabel table.
# 3. Menampilkan 5 baris pertama dari data menggunakan fungsi table.head().
# 4. Mengambil data NAMA KELURAHAN dari tabel dan menyimpannya ke dalam variabel x_label.
# 5. Membuat bar chart dengan menggunakan plt.bar(). Parameter x adalah array yang berisi index dari data, yaitu np.arange(len(x_label)), dan parameter height adalah data jumlah penduduk laki-laki WNI dari tabel.
# 6. Mengatur label sumbu x menggunakan `plt.xticks()` dengan label yang diambil dari kolom 'NAMA KELURAHAN' dan melakukan rotasi sebesar 30 derajat.
# 7. Menambahkan label sumbu x dan y menggunakan plt.xlabel() dan plt.ylabel().
# 8. Menambahkan judul plot menggunakan plt.title().
# 9. Menampilkan bar chart yang telah dibuat menggunakan plt.show().
