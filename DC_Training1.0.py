print("WELCOME TO THE LEARNING PYTHON")
print("Good Morning\nGood Afternoon\nGood Night")
print("Continue"+" to"+" innovate"+" and"+" always"+" have"+" a"+" creative"+" spirit")

# input() can take default value if no input given by the user.
print("Hello "+ input("What is your nama?"))

# len() function returns the number of characters in string.
print(len(input()))

# Variabel
name = input("What is your nama?")
length = len(name)
print(length)

# Input/Output
name = input('Masukan nama Anda: ')
print(name)

name = "Perseus Evans"
print("Hello, nama saya {name}")        # Metode Formatted String
print("Nama saya %s" % (name))          # Metode %-formatting
print("Nama saya {}".format(name))      # str.format()
