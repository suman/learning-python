import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# 0 means letters, 1 means numbers and 2 means symbols
characters = [0, 1, 2]

total_letters = ""
total_symbols = ""
total_numbers = ""

generated_password = ""
while True:
    if len (generated_password) == (nr_letters + nr_symbols + nr_numbers):
        break

    char_index = random.randint(0, 2)
    if char_index == 0 and len(total_letters) != nr_letters:
        letter_index = random.randint(0, len(letters) - 1)
        total_letters += letters[letter_index]
        generated_password += letters[letter_index]

    if char_index == 1 and len(total_symbols) != nr_symbols:
        symbol_index = random.randint(0, len(symbols) - 1)
        total_symbols += symbols[symbol_index]
        generated_password += symbols[symbol_index]

    if char_index == 2 and len(total_numbers) != nr_numbers:
        number_index = random.randint(0, len(numbers) - 1)
        total_numbers += numbers[number_index]
        generated_password += numbers[number_index]

print(f"Your new password is {generated_password}")
