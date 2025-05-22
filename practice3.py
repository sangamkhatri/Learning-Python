# Task: Create a function to print all even numbers from a list.
def print_even_numbers(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(num)


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 8.5]
print_even_numbers(my_list)

# Task: Create a function that prints student names and grades from a dictionary.


def print_student_grades(student_dict):
    for name, grade in student_dict.items():
        print(f"{name} scored {grade}")


students = {
    "Sangam": 88,
    "Abhinav": 92,
    "Nischal": 85,
    "Sanjeet": 90
}
print_student_grades(students)
# Task: Create a function that prints employee names and roles.


def print_employees(employees):
    for emp in employees:
        print(f"{emp['name']} works as a {emp['role']}")


employee_list = [
    {"name": "Sangam", "role": "Data Analyst"},
    {"name": "Abhinav", "role": "Project Manager"},
    {"name": "Nischal", "role": "Developer"}
]
print_employees(employee_list)

# Task: Return a list of squares of numbers.


def get_squares(numbers):
    squares = []
    for n in numbers:
        squares.append(n**2)
    return squares


nums = [1, 2, 3, 4, 5]
squares = get_squares(nums)
print(squares)
