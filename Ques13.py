# Program to ask the user for their birth year and calculate their age

# Importing the datetime module
import datetime

# Taking the user's birth year as input
birth_year = int(input("Enter your birth year: "))

# Calculating the current year
current_year = datetime.datetime.now().year

# Calculating the user's age
age = current_year - birth_year

# Printing the user's age
print(f"You are {age} years old.")
