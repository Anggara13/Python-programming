# Membuat Fungsi
def salam():
    print("Hello, Selamat Pagi")

## Pemanggilan Fungsi
salam()

def luas_segitiga(alas, tinggi): #alas dan tinggi merupakan parameter yang masuk
    luas = (alas * tinggi) / 2
    print("Luas segitiga: %f" % luas);

# Pemanggilan fungsi
##4 dan 6 merupakan parameter yang diinputkan kedalam fungsi luas segitiga
luas_segitiga(4, 6) 

#alas dan tinggi merupakan parameter yang masuk
def luas_segiemapat(sisipendek, sisipanjang):
    luas1 = (sisipendek * sisipanjang)
    return luas1


# Pemanggilan fungsi
##4 dan 6 merupakan parameter yang diinputkan kedalam fungsi luas segitiga 
print("Luas segiempat: %d" % luas_segiemapat(4, 6))
