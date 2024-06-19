# Program to take a list of numbers and return their sum

# Taking a list of numbers as input from the user
numbers = input("Enter a list of numbers separated by spaces: ").split()

# Converting the input strings to integers
numbers = [int(num) for num in numbers]

# Calculating the sum of the numbers
total_sum = sum(numbers)

# Printing the sum of the numbers
print(f"The sum of the numbers is: {total_sum}")
