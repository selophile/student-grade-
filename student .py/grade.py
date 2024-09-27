# Student Grade Management System

# List to store student data
students = []

def calculate_grade(total_score):
    if total_score >= 90:
        return 'A'
    elif total_score >= 80:
        return 'B'
    elif total_score >= 70:
        return 'C'
    elif total_score >= 60:
        return 'D'
    else:
        return 'F'

# Function to add student information
def add_student():
    name = input("Enter student's name: ")
    student_id = input("Enter student ID: ")
    scores = []
    for i in range(3):
        score = float(input(f"Enter score for subject {i + 1}: "))
        scores.append(score)

    total_score = sum(scores) / 3 
     # Calculate the average score
    grade = calculate_grade(total_score)

    student = {
        'name': name,
        'student_id': student_id,
        'scores': scores,
        'total_score': total_score,
        'grade': grade
    }
    students.append(student)

# Function to display all students' information
def display_students():
    if not students:
        print("No student data available.")
        return

    for student in students:
        print("\nStudent Name:", student['name'])
        print("Student ID:", student['student_id'])
        print("Scores:", student['scores'])
        print("Total Score:", student['total_score'])
        print("Grade:", student['grade'])

# Main loop
while True:
    print("\nStudent Grade Management System")
    print("1. Add a student")
    print("2. Display all students")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        print("Exiting the system.")
    break
else:
      print("Invalid choice. Please try again.")