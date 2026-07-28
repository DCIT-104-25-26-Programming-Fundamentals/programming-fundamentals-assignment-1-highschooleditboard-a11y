# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================

def read_matrix(name, rows, cols):
    matrix = []
    print(f"Enter {name} ({rows}x{cols}):")
    for i in range(rows):
        while True:
            row = input(f"  Enter row {i + 1}: ").split()
            if len(row) == cols:
                matrix.append([float(x) for x in row])
                break
            print(f"  Error: please enter exactly {cols} values.")
    return matrix

def display_matrix(matrix):
    for row in matrix:
        print("  " + "  ".join(f"{val:6.1f}" for val in row))

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        result.append(new_row)
    return result

def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = []
    for r in range(rows):
        new_row = []
        for c in range(cols):
            new_row.append(matrix_a[r][c] + matrix_b[r][c])
        result.append(new_row)
    return result

def multiply_matrices(matrix_a, matrix_b):
    m = len(matrix_a)
    n = len(matrix_a[0])
    p = len(matrix_b[0])
    # Build result matrix filled with zeros
    result = [[0] * p for _ in range(m)]
    for r in range(m):
        for c in range(p):
            for k in range(n):
                result[r][c] += matrix_a[r][k] * matrix_b[k][c]
    return result

def main():
    # --- Part A: Transpose ---
    print("=" * 40)
    print("PART A — Matrix Transpose")
    print("=" * 40)
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix("matrix", rows, cols)
    print("\nOriginal Matrix:")
    display_matrix(matrix)
    print("\nTransposed Matrix:")
    display_matrix(transpose(matrix))

    # --- Part B: Addition ---
    print("\n" + "=" * 40)
    print("PART B — Matrix Addition")
    print("=" * 40)
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix_a = read_matrix("Matrix A", rows, cols)
    matrix_b = read_matrix("Matrix B", rows, cols)
    print("\nMatrix A:")
    display_matrix(matrix_a)
    print("\nMatrix B:")
    display_matrix(matrix_b)
    print("\nA + B:")
    display_matrix(add_matrices(matrix_a, matrix_b))

    # --- Part C: Multiplication ---
    print("\n" + "=" * 40)
    print("PART C — Matrix Multiplication")
    print("=" * 40)
    m = int(input("Enter rows for Matrix A: "))
    n = int(input("Enter columns for Matrix A (= rows for Matrix B): "))
    p = int(input("Enter columns for Matrix B: "))
    matrix_a = read_matrix("Matrix A", m, n)
    matrix_b = read_matrix("Matrix B", n, p)
    print("\nMatrix A:")
    display_matrix(matrix_a)
    print("\nMatrix B:")
    display_matrix(matrix_b)
    print("\nA x B:")
    display_matrix(multiply_matrices(matrix_a, matrix_b))

main()
