# Function to calculate average of a list
def calculate_average(scores):
    return sum(scores) / len(scores)

# Function to print student info with average


def print_student_averages(students):
    print("Student Averages:")
    for student in students:
        avg = calculate_average(student["grades"])
        print(
            f"{student['name']} from {student['city']} has an average grade of {avg:.2f}")

# Function to print subject-wise averages


def print_subject_averages(subject_scores):
    print("\nSubject Averages:")
    for subject, scores in subject_scores.items():
        avg = calculate_average(scores)
        print(f"{subject}: {avg:.2f}")


# List of students
students = [
    {"name": "Sita", "grades": [85, 90, 88], "city": "Kathmandu"},
    {"name": "Ram", "grades": [78, 80, 75], "city": "Pokhara"},
    {"name": "Hari", "grades": [92, 88, 95], "city": "Lalitpur"}
]

# Dictionary of subject-wise scores
subject_scores = {
    "Math": [85, 78, 92],
    "Science": [90, 80, 88],
    "English": [88, 75, 95]
}

# Add new subject
subject_scores["History"] = [82, 70, 89]

# Call functions to display results
print_student_averages(students)
print_subject_averages(subject_scores)
