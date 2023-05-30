import random

letters=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols=["!", "@", "#", "$", "%", "&", "*", "(", "=", "^"]
password=[]

print("Welcome to password generator")

nr_letters=int(input("How many letters would your like in your password? "))
nr_numbers=int(input("How many numbers would your like in your password? "))
nr_symbols=int(input("How many symbols would your like in your password? "))

choosed_letters=random.sample(letters, nr_letters)
choosed_numbers=random.sample(numbers, nr_numbers)
choosed_symbols=random.sample(symbols, nr_symbols)
password.extend(choosed_letters)
password.extend(choosed_numbers)
password.extend(choosed_symbols)

random.shuffle(password)

print("Generated Password:\n {}".format(''.join(password)))
 




