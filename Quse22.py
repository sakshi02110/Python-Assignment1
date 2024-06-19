# Program to return the minimum and maximum values in a list of numbers

# Taking a list of numbers as input from the user
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Finding the minimum and maximum values
min_value = min(numbers)
max_value = max(numbers)

# Printing the minimum and maximum values
print(f"The minimum value in the list is {min_value}.")
print(f"The maximum value in the list is {max_value}.")
