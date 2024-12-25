# Type error, Type Checking and Type Convertion

num_char = len(input("What is your name?"))
print ("The length of your name is ", num_char) 
# Type Checking
print(type(num_char))

new_num_char = str(num_char)
# Type Convertion
# to String code = str
# to Interger code = int
# to Float code = float

print("Your name has "+ new_num_char + " characters.")

# Example with Number
a = (123)

print(70 + float("100.5"))

print("Aca" + str(13062000))

age = 17
salary = 5000000.0

print(type(age))        #int
print(type(salary))     #float

x = 6
print(type(x))          #int

x = 'Dicoding'
print(type(x))          #str single quote
print(x[0])             #mengakses setiap karakter dari string (substring) dengan menggunakan metode indexing
print(x[2:])            #metode slicing

x = "6"
print(type(x))          #str double quote

multi_line = """Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu."""

print(multi_line)

x = 1+2j
print(type(x))          #complex

# Ini membuktikan bahwa Number bersifat immutable
var = 10
print(var)
print(id(var))
var = 11
print(var)
print(id(var))

# Data Tipe Boolean
x = True
print(type(x))

x = False
print(type(x))
