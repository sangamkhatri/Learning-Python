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
