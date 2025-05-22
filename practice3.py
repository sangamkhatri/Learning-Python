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
