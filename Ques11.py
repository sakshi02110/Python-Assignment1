# Program to generate the first n numbers in the Fibonacci sequence

# Function to generate Fibonacci sequence
def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

# Taking the number of terms as input from the user
n = int(input("Enter the number of terms in the Fibonacci sequence: "))

# Generating the Fibonacci sequence
fib_sequence = fibonacci(n)

# Printing the Fibonacci sequence
print(f"The first {n} numbers in the Fibonacci sequence are: {fib_sequence}")
