# Program to read the content of a text file and print it to the console

# Reading the content of the text file
with open("output.txt", "r") as file:
    content = file.read()

# Printing the content to the console
print("The content of the file is:")
print(content)
