# Program to check if two strings are anagrams of each other

# Taking two strings as input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Checking if the two strings are anagrams
if sorted(string1) == sorted(string2):
    print(f"'{string1}' and '{string2}' are anagrams.")
else:
    print(f"'{string1}' and '{string2}' are not anagrams.")
