# Program to remove all punctuation from a given string

import string

# Taking a string as input from the user
user_string = input("Enter a string: ")

# Removing all punctuation from the string
clean_string = user_string.translate(str.maketrans("", "", string.punctuation))

# Printing the string without punctuation
print(f"The string without punctuation is: {clean_string}")
