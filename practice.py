# logic building
"""Logic Questions
Sum of Digits – sum_of_digits(n)

Check Prime – is_prime(n)

Reverse a Number – reverse_number(n)

Count Vowels in a String – count_vowels(s)

Fibonacci Series up to n terms – fibonacci(n)"""


def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def reverse_number(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev


def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)


def fibonacci(n):
    fib = []
    a, b = 0, 1
    for _ in range(n):
        fib.append(a)
        a, b = b, a + b
    return fib


# Sample calls to test the functions
print("Sum of digits (1234):", sum_of_digits(1234))
print("Is 29 prime?:", is_prime(29))
print("Reverse of 1234:", reverse_number(1234))
print("Vowels in 'Hello World':", count_vowels("Hello World"))
print("Fibonacci (first 7 numbers):", fibonacci(7))
""""