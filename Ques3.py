 # Program to calculate the factorial of a given number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
num = int(input("Enter a number to find its factorial : "))
result = factorial(num)
print(f"The factorial of {num} is {result} . ")


    
