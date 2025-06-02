"""Let’s create a small Python program that involves:

Lists

Dictionaries

Classes

File Input/Output (I/O)
 Mini Project Idea: Student Grade Tracker
We will:

Create a Student class.

Store multiple students in a list.

Use a dictionary to map student names to grades.

Read and write the student data to a file."""
import json


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades  # a list of integers

    def average(self):
        return sum(self.grades) / len(self.grades)

    def to_dict(self):
        return {'name': self.name, 'grades': self.grades}

    @staticmethod
    def from_dict(data):
        return Student(data['name'], data['grades'])


# Create some students and store them in a list
students = [
    Student("Alice", [85, 90, 78]),
    Student("Bob", [70, 88, 92]),
    Student("Charlie", [95, 100, 98])
]

# Write to file
with open("students.txt", "w") as f:
    data = [student.to_dict() for student in students]
    json.dump(data, f)

# Read from file
with open("students.txt", "r") as f:
    loaded_data = json.load(f)
    loaded_students = [Student.from_dict(d) for d in loaded_data]

# Display student averages
for student in loaded_students:
    print(f"{student.name}'s average grade: {student.average():.2f}")
