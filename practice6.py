# Global dictionary to store student data
students = {}


def add_student(name, subjects):
    """Adds a student with a dictionary of subjects and marks."""
    students[name] = subjects
    print(f"Added {name}")


def update_marks(name, subject, new_mark):
    """Updates the mark for a given subject of a student."""
    if name in students and subject in students[name]:
        students[name][subject] = new_mark
        print(f"Updated {name}'s {subject} mark to {new_mark}")
    else:
        print("Student or subject not found.")


def calculate_average(name):
    """Calculates and returns the average marks of a student."""
    if name in students:
        marks = students[name].values()
        average = sum(marks) / len(marks)
        return average
    else:
        print("Student not found.")
        return None


def display_all_students():
    """Prints all student data."""
    for name, subjects in students.items():
        print(f"\n{name}:")
        for subject, mark in subjects.items():
            print(f"  {subject}: {mark}")
        avg = calculate_average(name)
        print(f"  Average: {avg:.2f}")


# Example usage
add_student("Alice", {"Math": 90, "Science": 85})
add_student("Bob", {"Math": 75, "English": 80})
update_marks("Alice", "Math", 95)
display_all_students()
