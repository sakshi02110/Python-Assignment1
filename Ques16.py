# Program to count the frequency of each character in a string

# Taking a string as input from the user
user_string = input("Enter a string: ")

# Counting the frequency of each character
frequency = {}
for char in user_string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

# Printing the frequency of each character
print("Character frequency:")
for char, count in frequency.items():
    print(f"{char}: {count}")
