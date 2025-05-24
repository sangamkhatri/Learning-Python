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

# 1. Create a list
fruits = ["apple", "banana", "cherry"]
print("Initial list:", fruits)

# 2. Access the second item
print("Second item:", fruits[1])

# 3. Change 'banana' to 'blueberry'
fruits[1] = "blueberry"
print("After changing second item:", fruits)

# 4. Add 'orange' to the end
fruits.append("orange")
print("After appending 'orange':", fruits)

# 5. Remove 'apple' from the list
fruits.remove("apple")
print("After removing 'apple':", fruits)

# 6. Create a list and print its length
numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)
print("Length of the list:", len(numbers))

# 7. Calculate and print the sum
total = sum(numbers)
print("Sum of numbers:", total)

# 8. Loop through the list and print each item
print("Looping through list:")
for num in numbers:
    print("Number:", num)

# 9. Check if 30 is in the list
if 30 in numbers:
    print("Found 30 in the list")
else:
    print("30 Not found")

# 10. Sort the list in reverse order
numbers.sort(reverse=True)
print("List sorted in descending order:", numbers)

# 1. Create a nested list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix:")
for row in matrix:
    print(row)

# 2. Access a specific element (e.g., element at row 2, column 3)
print("Element at 2nd row, 3rd column:", matrix[1][2])  # Output: 6

# 3. Flatten the matrix using a nested loop
flattened = []
for row in matrix:
    for num in row:
        flattened.append(num)
print("Flattened list:", flattened)

# 4. Use list comprehension to get only even numbers from the flattened list
even_numbers = [num for num in flattened if num % 2 == 0]
print("Even numbers:", even_numbers)

# 5. Define a function to return squares of all numbers in a list


def square_list(lst):
    return [x**2 for x in lst]


squared = square_list(flattened)
print("Squares of numbers:", squared)

# 6. Filter numbers greater than 5 from the squared list using a function


def filter_greater_than_five(lst):
    return [x for x in lst if x > 5]


filtered = filter_greater_than_five(squared)
print("Numbers > 5 in squared list:", filtered)
