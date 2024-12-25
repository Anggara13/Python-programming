# Tipe data colection

# 1. List data
x = [1, 2.2, 'Dicoding']
print(type(x))
# Metode indexing
x = [1, 'Dicoding', True, 1.0]
print(x[2])

x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]
print(x[0])
print(x[2])
print(x[-1])    # data paling terakhir
print(x[-3])    # data yang ke 3 dari urutan terakhir

# List bersifat mutable
x = [1, 2.2, 'Dicoding']
x[0] = 'Indonesia'
print(x)