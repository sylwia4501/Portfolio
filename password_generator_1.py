import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

length_letters = len(letters)
list_letters = []
for letter in range(nr_letters):
  letter = random.randint(0, length_letters - 1)
  letter = letters[letter]
  list_letters.append(letter)

length_symbols = len(symbols)
list_symbols = []
for symbol in range(nr_symbols):
  symbol = random.randint(0, length_symbols - 1)
  symbol = symbols[symbol]
  list_symbols.append(symbol)
  
length_numbers = len(numbers)
list_numbers = []
for number in range(nr_numbers):
  number = random.randint(0, length_numbers - 1)
  number = numbers[number]
  list_numbers.append(number)

password = list_letters + list_symbols + list_numbers
print(password)

random.shuffle(password)
randomised_password = ''.join(password)
print(password)
print(f"Your password is: {randomised_password}")
