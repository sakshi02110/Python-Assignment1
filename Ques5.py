# Program to take a string input from the user and write it to a text file

# Taking a string input from the user
user_input = input("Enter a string to write to the file: ")

# Writing the string to a text file
with open("output.txt", "w") as file:
    file.write(user_input)

print("The string has been written to 'output.txt'.")
