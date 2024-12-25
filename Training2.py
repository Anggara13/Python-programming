# IF / ELSE / ELIF Statment

# Pengunaan IF saja
i = 7 #inisialisasi variable i yang memiliki nilai 10

if(i==10): #pengecekan nilai i apakah sama dengan 10
    print("ini adalah angka 10") #jika TRUE maka akan mencetak kalimat ini

# Penggunaan IF...ELSE...
A = 5 #inisialisasi variable i yang memiliki nilai 10

if(A==10): #pengecekan nilai i apakah sama dengan 10
    print("ini adalah angka 10") #jika TRUE maka akan mencetak kalimat ini
else:
    print("bukan angka 10") #jika FALSE akan mencetak kalimat ini

# Pengunaan IF...ELIF...ELSE...
B=3

if(B==5):
     print("ini adalah angka 5")
elif(B>5):
     print("lebih besar dari 5")
else:
     print("lebih kecil dari 5")

# Nested IF atau pengunaan IF bertingkat
C=2
if (C<7):
	print("nilai i kurang dari 7")
	if (C<3):
		print("nilai i kurang dari 7 dan kurang dari 3")
	else:
		print("nilai i kurang dari 7 tapi lebih dari 3")