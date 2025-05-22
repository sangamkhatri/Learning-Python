# Task: Create a function to print all even numbers from a list.
def print_even_numbers(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(num)


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 8.5]
print_even_numbers(my_list)
