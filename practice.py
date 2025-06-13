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
""""Check Armstrong Number – e.g., 153 → 1³ + 5³ + 3³ = 153

Check Palindrome (number) – same forward and backward

Find LCM of two numbers

Pattern Printing – Right triangle of stars (e.g., for n = 5)"""


def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return sum(int(d)**power for d in digits) == n


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def lcm(a, b):
    greater = max(a, b)
    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1


def print_triangle(n):
    for i in range(1, n + 1):
        print('*' * i)

# Example function calls


print("Is 153 Armstrong?:", is_armstrong(153))
print("Is 121 Palindrome?:", is_palindrome(121))
print("LCM of 12 and 18:", lcm(12, 18))
print("Triangle of 5 rows:")
print_triangle(5)
"""Check Perfect Number
– A number where the sum of its proper divisors equals the number.
Example: 28 → 1 + 2 + 4 + 7 + 14 = 28

Find All Factors of a Number

Count Words in a Sentence

Check for a Prime Number in a Range

Sum of Even and Odd Digits Separately"""


def is_perfect(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n


def find_factors(n):
    return [i for i in range(1, n+1) if n % i == 0]


def count_words(sentence):
    return len(sentence.strip().split())


def primes_in_range(start, end):
    return [n for n in range(start, end+1) if is_prime(n)]


def sum_even_odd_digits(n):
    even_sum = 0
    odd_sum = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
        n //= 10
    return even_sum, odd_sum


# Example calls for new logic
print("Is 28 perfect?:", is_perfect(28))
print("Factors of 18:", find_factors(18))
print("Words in 'Hello world from Python':",
      count_words("Hello world from Python"))
print("Prime numbers between 10 and 30:", primes_in_range(10, 30))
even, odd = sum_even_odd_digits(123456)
print("Even and Odd digit sum of 123456:", even, odd)
