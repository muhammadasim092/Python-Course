# FIBONACCI GENERATOR

# The Fibonacci series is a sequence where each number is
# the sum of the two preceding numbers, defined by a
# mathematical recurrence relationship.

def generate_fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

try:
    terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
    if terms <= 0:
        print("Please enter a positive integer.")
    else:
        sequence = generate_fibonacci(terms)
        print("Fibonacci sequence:")
        print(sequence)
except ValueError:
    print("Invalid input. Please enter an integer.")
