# Program to check if a string starts with a given prefix or ends with a given suffix

# Taking the string, prefix, and suffix as input from the user
user_string = input("Enter a string: ")
prefix = input("Enter the prefix to check: ")
suffix = input("Enter the suffix to check: ")

# Checking if the string starts with the given prefix
if user_string.startswith(prefix):
    print(f"The string starts with the prefix '{prefix}'.")
else:
    print(f"The string does not start with the prefix '{prefix}'.")

# Checking if the string ends with the given suffix
if user_string.endswith(suffix):
    print(f"The string ends with the suffix '{suffix}'.")
else:
    print(f"The string does not end with the suffix '{suffix}'.")
