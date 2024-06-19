def get_sum_of_digits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

try:
    num = int(input("Enter a number: "))
    print("Sum of digits:", get_sum_of_digits(num))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
