"""Assume the existence of a function named check_uv_level with the method header below:

def check_uv_level(n : int) -> str:

Call the check_uv_level function with the value 10 and assign the result to a variable named uv_level"""


def check_uv_level(uv_index):
    if uv_index < 3:
        return "Low risk"
    elif uv_index < 6:
        return "Moderate risk"
    elif uv_index < 8:
        return "High risk"
    elif uv_index < 11:
        return "Very high risk"
    else:
        return "Extreme risk"


print(check_uv_level(3))

"""Given the following incomplete template of add. Complete the function such that it takes two inputs (int, int) and returns their sum"""


def add(a, b):
    return a + b


print(add(3, 5))

"""Assume the existence of a function named calculate_discounted_price with the method header below

def calculate_discounted_price ( original_price: float, discount_percentage: float) -> float:

Call the calculate_discounted_price function with the value 100.0 and 25.0 and save the result into the variable named final_price"""


def calculate_discounted_price(original_price, discount_percentage):
    if discount_percentage <= 0:
        return original_price
    elif discount_percentage >= 100:
        return 0.0  # Free item
    return (original_price * (1 - discount_percentage / 100)) * 0.5


print(calculate_discounted_price(100.0, 25.0))

"""Given the following incomplete template of is_even. Complete the function such that it takes one input (int) and returns
True if the input is even, 
False otherwise."""


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


print(is_even(42))
print(is_even(-13))
print(is_even(7))
"""Assume the existence of two functions named foo and bar with the method headers below:

def foo(n : int) -> int:

def bar(n : int) -> int:

Call the foo function with the value 10 and assign the result to a variable named foo_out

Call the bar function with the value 3 and assign the result to a variable named bar_out.

Create a variable named calculation which stores the sum of the two variables."""


def foo(n: int) -> int:
    return n


def bar(n: int) -> int:
    return n


foo_out = foo(10)
print(foo_out)
bar_out = bar(3)
print(bar_out)
calculation = foo_out+bar_out
print(calculation)

"""Define a function named the_same that takes two inputs (bool, bool) and returns
True if both inputs are the same
False otherwise."""


def the_same(a, b):
    if a == b:
        return True
    else:
        return False


print(the_same(True, True))
print(the_same(True, False))
print(the_same(False, True))
print(the_same(False, False))

"""Given the function named bar that takes a string input. The function should return the string in lower case.

Press check to debug the code and fix the error."""


def bar(s):
    return s.lower()


print(bar("SANGAM"))
"""Define a function named soup that takes a string input and prints the string in reverse"""


def soup(a):
    print(a[::-1])


soup("sangam")

"""Define a function named bat that takes a string input and returns the string in reverse"""


def bat(n):
    return n[::-1]


print(bat("sangam"))

"""Define a function named sarah that takes a string input and prints a string containing every 2nd character starting from index 1 to the 3rd last index (exclusive)."""


def sarah(n):
    print(n[1:-3:2])


sarah("sangam is okay and she is okay")
"""Define a function named bbq_sauce that takes a string input and returns a string containing every 3rd character starting from index 2 to the 3rd last index (exclusive)."""


def bbq_sauce(n):
    return n[2:-2:3]


print(bbq_sauce("sangam is sangam and this is why"))
"""Define a function named print_in_range that takes two int values (say start, and end) and prints all numbers between start and end (inclusive)."""


def print_in_range(start, end):
    for i in range(start, end+1):
        print(i)


print_in_range(1, 10)

"""Define a function named odds_in_range that takes two int values (say start, and end) and counts all numbers between start and end (inclusive) that are odd."""
