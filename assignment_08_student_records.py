# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# TASK: Student Record Management System
# =============================================================================


def show_menu():
    """Display the menu options."""
    print("================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def add_student(students):
    """Prompt for student details and scores, then add the record."""
    name = input("Student name: ")
    student_id = input("Student ID: ")

    try:
        num_scores = int(input("How many scores? "))
    except ValueError:
        print("Error: number of scores must be a whole number.")
        return

    if num_scores <= 0:
        print("Error: number of scores must be positive.")
        return

    scores = []
    for i in range(1, num_scores + 1):
        score_input = input(f"Enter score {i}: ")
        try:
            scores.append(float(score_input))
        except ValueError:
            print(f"Error: '{score_input}' is not a valid number. Score skipped.")

    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    students.append(student)
    print(f'Student "{name}" added successfully.')


def calculate_average(scores):
    """Return the average of a list of scores, rounded to 2 decimals."""
    if not scores:
        return 0.0
    return round(sum(scores) / len(scores), 2)


def display_students(students):
    """Print a formatted table of all students, their scores, and averages."""
    if not students:
        print("No students have been added yet.")
        return

    print("-" * 50)
    print(f"{'Name':<15}{'ID':<12}{'Scores':<15}{'Average':<10}")
    print("-" * 50)
    for student in students:
        scores_str = ", ".join(str(int(s)) if s.is_integer() else str(s) for s in student["scores"])
        avg = calculate_average(student["scores"])
        print(f"{student['name']:<15}{student['id']:<12}{scores_str:<15}{avg:<10}")
    print("-" * 50)


def find_student_average(students):
    """Look up a student by ID and display their average score."""
    student_id = input("Enter student ID: ")

    for student in students:
        if str(student["id"]) == student_id:
            avg = calculate_average(student["scores"])
            print(f"{student['name']}'s average score: {avg}")
            return

    print(f"Error: no student found with ID {student_id}.")


def main():
    students = []

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            find_student_average(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: invalid choice. Please enter a number from 1 to 4.")

        print()  # blank line for readability


if __name__ == "__main__":
    main()
