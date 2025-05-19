"""2. Calculate factorial (without recursion)"""


def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


# Function call
print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1

""" Check if a string is a palindrome"""


def is_palindrome(s):
    return s == s[::-1]


# Function call
print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False

""" Count vowels in a string"""


def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


# Function call
print(count_vowels("Hello World"))  # Output: 3

""" Check if a number is prime"""


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


# Function call
print(is_prime(7))   # Output: True
print(is_prime(10))  # Output: False

""" Fibonacci series up to n terms"""


def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


# Function call
print(fibonacci(6))  # Output: [0, 1, 1, 2, 3, 5]

"""Reverse a number"""


def reverse_number(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return rev


# Function call
print(reverse_number(1234))  # Output: 4321

""". Print a Right-Angled Triangle Pattern"""


def triangle_pattern(n):
    for i in range(1, n + 1):
        print("* " * i)


# Function call
triangle_pattern(5)

""". Print a Pyramid Pattern"""


def pyramid_pattern(n):
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '* ' * i
        print(spaces + stars)


# Function call
pyramid_pattern(5)
