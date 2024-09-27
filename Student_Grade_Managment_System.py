# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 22:43:22 2024

@author:RITU BHARTI
"""

# Student Grade Management System

# Function to calculate total score and overall grade
def calculate_grade(scores):
    total_score = sum(scores.values())
    average_score = total_score / len(scores)

    if average_score >= 90:
        grade = 'A'
    elif average_score >= 80:
        grade = 'B'
    elif average_score >= 70:
        grade = 'C'
    elif average_score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    return total_score, grade

# Function to add a student
def add_student(student_data):
    name = input("Enter student's name: ")
    student_id = input("Enter student ID: ")
    
    # Collect scores for at least 3 subjects
    scores = {}
    subjects = ["Math", "Science", "English"]
    
    for subject in subjects:
        score = float(input(f"Enter score for {subject}: "))
        scores[subject] = score
    
    # Calculate total score and grade
    total_score, overall_grade = calculate_grade(scores)
    
    # Store the student data
    student_data[student_id] = {
        'name': name,
        'scores': scores,
        'total_score': total_score,
        'overall_grade': overall_grade
    }

# Function to display all students' data
def display_students(student_data):
    if not student_data:
        print("No student data available.")
        return
    
    for student_id, data in student_data.items():
        print(f"\nStudent ID: {student_id}")
        print(f"Name: {data['name']}")
        print("Scores:")
        for subject, score in data['scores'].items():
            print(f"  {subject}: {score}")
        print(f"Total Score: {data['total_score']}")
        print(f"Overall Grade: {data['overall_grade']}")

def main():
    student_data = {}
    
    while True:
        action = input("\nDo you want to add a student? (yes/no): ").lower()
        if action == 'yes':
            add_student(student_data)
        elif action == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    
    display_students(student_data)

if __name__ == "__main__":
    main()
