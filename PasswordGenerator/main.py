import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator")
chosen_letters = int(input("How many letters would you like in your password? "))
chosen_symbols = int(input("How many symbols would you like? "))
chosen_numbers = int(input("How many numbers would you like? "))

generated_password = ""

for letter in range(0, chosen_letters):
    rand_index = random.randint(0, len(letters) - 1)
    generated_password += letters[rand_index]

for symbol in range(0, chosen_symbols):
    rand_index = random.randint(0, len(symbols) - 1)
    generated_password += symbols[rand_index]

for number in range(0, chosen_numbers):
    rand_index = random.randint(0, len(numbers) - 1)
    generated_password += numbers[rand_index]

# Converted to list to use shuffle function

generated_password_list = list(generated_password)
random.shuffle(generated_password_list)

# After in correct order we add each character to an empty string

generated_password_string = ""

for character in generated_password_list:
    generated_password_string += character

print("Your password is: " + generated_password_string)
