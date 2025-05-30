students = [
    {"name": "Alice", "grade": 90},
    {"name": "Bob", "grade": 85},
    {"name": "Charlie", "grade": 92}
]

# Print all names and grades
for student in students:
    print(f"{student['name']} got {student['grade']}")
# List of subjects
subjects = ["Math", "Science", "English", "History"]

# Dictionary of student profiles
student1 = {
    "name": "Sita",
    "grades": [85, 90, 88],
    "city": "Kathmandu"
}

student2 = {
    "name": "Ram",
    "grades": [78, 80, 75],
    "city": "Pokhara"
}

student3 = {
    "name": "Hari",
    "grades": [92, 88, 95],
    "city": "Lalitpur"
}

# List of students (list of dictionaries)
students = [student1, student2, student3]

# Print all students and their average grade
for student in students:
    avg = sum(student["grades"]) / len(student["grades"])
    print(
        f"{student['name']} from {student['city']} has an average grade of {avg}")

# Create a dictionary with subject as key and list of scores as value
subject_scores = {
    "Math": [85, 78, 92],
    "Science": [90, 80, 88],
    "English": [88, 75, 95]
}

# Calculate and print average per subject
print("\nAverage scores by subject:")
for subject, scores in subject_scores.items():
    avg = sum(scores) / len(scores)
    print(f"{subject}: {avg:.2f}")

# Add a new subject and scores
subject_scores["History"] = [82, 70, 89]

# Print updated subject scores
print("\nUpdated Subjects and Scores:")
for subject, scores in subject_scores.items():
    print(f"{subject} → {scores}")
