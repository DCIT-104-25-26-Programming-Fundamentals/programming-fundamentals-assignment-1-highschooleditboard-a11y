# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================

def print_fibonacci(n):
    # Validate input
    if n <= 0:
        print("Error: Please enter a positive integer.")
        return

    # Generate first N terms using a loop
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    print("Fibonacci sequence: " + " ".join(str(x) for x in sequence))

def is_fibonacci(number):
    # Handle negative numbers
    if number < 0:
        print(f"{number} is NOT a Fibonacci number.")
        return

    # Generate Fibonacci numbers until we reach or pass the input
    a, b = 0, 1
    while a < number:
        a, b = b, a + b

    # If a equals the number exactly, it's in the sequence
    if a == number:
        print(f"{number} is a Fibonacci number.")
    else:
        print(f"{number} is NOT a Fibonacci number.")

def main():
    # Part A
    print("PART A — First N Fibonacci Terms")
    n = int(input("How many terms? "))
    print_fibonacci(n)

    # Part B
    print("\nPART B — Fibonacci Checker")
    number = int(input("Enter a number to check: "))
    is_fibonacci(number)

main()
