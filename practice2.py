"""2. Calculate factorial (without recursion)"""


def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


# Function call
print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
