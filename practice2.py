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
