# Program to read multiple lines of input from the user until they enter an empty line, then print all the lines

print("Enter multiple lines of input (enter an empty line to stop):")

# Reading lines of input from the user
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

# Printing all the lines
print("You entered:")
for line in lines:
    print(line)
