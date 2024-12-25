# Perulangan atau Lupping

# WHILE
#nilai awal j =0
j = 0 

#ketika j kurang dari 6 lakukan perulangan, jika tidak stop perulangan
while j<6: 
    #lakukan perintah ini ketika perulangan
    print("Ini adalah perulangan ke -",j) 
    #setiap kali diakhir perulangan update nilai dengan ditambah 1.
    j=j+1 

# FOR
for i in range(1,6): #perulangan for sebagai inisialisasi dari angka 1 hingga angka yang lebih kecil daripada 6.

    print("Ini adalah perulangan ke -", i) #perintah jika looping akan tetap berjalan

count=[1,2,3,4,5] #elemen list

for number in count: #looping untuk menampilkan semua elemen pada count
    print("Ini adalah element count : ", number) #menampilkan elemen list pada count

for A in range(1,11):
    if(A%2==0):
        print("Angka genap",A)
    else:
        print("Angka ganjil",A)