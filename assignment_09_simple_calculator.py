# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# TASK: Console-Based Simple Calculator
# =============================================================================


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    """Divide a by b, rounded to 2 decimal places. Returns None if b is 0."""
    if b == 0:
        print("Error: Cannot divide by zero.")
        return None
    return round(a / b, 2)


def modulus(a, b):
    """Return a % b. Returns None if b is 0."""
    if b == 0:
        print("Error: Cannot divide by zero.")
        return None
    return a % b


def exponentiate(a, b):
    return a ** b


def show_menu():
    """Display the calculator menu."""
    print("============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def get_numbers():
    """Prompt for two numbers, returning None if input is invalid."""
    try:
        a = float(input("Enter first number : "))
        b = float(input("Enter second number: "))
        return a, b
    except ValueError:
        print("Error: please enter valid numbers.")
        return None


def format_number(n):
    """Display whole numbers without a trailing .0, like the example output."""
    return int(n) if float(n).is_integer() else n


def main():
    operations = {
        "1": ("+", add),
        "2": ("-", subtract),
        "3": ("*", multiply),
        "4": ("/", divide),
        "5": ("%", modulus),
        "6": ("**", exponentiate),
    }

    while True:
        show_menu()
        choice = input("Select an operation (1-7): ")

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in operations:
            print("Error: invalid choice. Please select a number from 1 to 7.")
            print()
            continue

        symbol, operation = operations[choice]
        numbers = get_numbers()

        if numbers is None:
            print()
            continue

        a, b = numbers
        result = operation(a, b)

        if result is not None:
            print(f"Result: {format_number(a)} {symbol} {format_number(b)} = {format_number(result)}")

        print()  # blank line for readability


if __name__ == "__main__":
    main()
