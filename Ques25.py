# Program to copy the contents of one text file to another

# Taking the source and destination file names as input from the user
source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")

# Copying the contents of the source file to the destination file
with open(source_file, 'r') as src:
    content = src.read()
    with open(destination_file, 'w') as dest:
        dest.write(content)

print(f"The contents of {source_file} have been copied to {destination_file}.")
