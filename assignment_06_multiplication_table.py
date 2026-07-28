# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================


def print_table(number):
    """Print the multiplication table for a single number, 1 to 12."""
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number}  x  {i:<2} =  {number * i}")


def print_tables_up_to_n(n):
    """Print multiplication tables for every number from 1 to n."""
    for number in range(1, n + 1):
        print_table(number)
        print("-" * 29)


def get_positive_int(prompt):
    """Ask for input and validate it's a positive integer. Stops on failure."""
    value = input(prompt)
    if not value.isdigit() or int(value) <= 0:
        print("Error: please enter a positive integer.")
        exit()
    return int(value)


def main():
    # Part A
    num = get_positive_int("Enter a number for its multiplication table: ")
    print_table(num)

    print()  # blank line separator between Part A and Part B

    # Part B (bonus)
    n = get_positive_int("Enter N to print tables from 1 to N: ")
    print_tables_up_to_n(n)


if __name__ == "__main__":
    main()
