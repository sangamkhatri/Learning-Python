"""Given a string theString, print how many times two consecutive, identical letters appear in the string. E.g.

"baa" has 1 pair.
"aha!!" has 0 pairs. "!" isn't a letter, and the "a"s aren't consecutive.
"Aah" has 0 pairs. The "A" and "a" are different.
(Consecutive: next to each other.)"""
theString = "saangaam"  # You can change this to test other inputs

count = 0
for i in range(len(theString) - 1):
    if theString[i].isalpha() and theString[i] == theString[i + 1]:
        count += 1

print("Number of pairs:", count)

"""Sum of even numbers between 1 and 100."""
sum = 0
for i in range(1, 100):
    if i % 2 == 0:
        sum = +i
print(sum)

"""Find factorial of a number using a loop."""

n = int(input("Enter a number: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print("Factorial of", n, "is", factorial)

"""Print multiplication table of a number n up to 10."""
num = int(input("enter a number"))
for i in range(1, 11):
    print(str(n) + "x" + str(i)+"=" + str(n*i))

"""Reverse a number (e.g., 123 → 321) using a loop."""
num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10        # Get the last digit
    reverse = reverse * 10 + digit  # Append digit to reverse
    num = num // 10         # Remove the last digit

print("Reversed number:", reverse)

"""Assume the existence of a function get_score that takes a single string input and returns an int.
(⚠️ get_score may crash if the inputs aren't strings!)

Complete the function compare_scores so that it returns...

None, if stringA or stringB are not strings.
-1, if stringA has a strictly lower score than stringB,
1, if stringA has a strictly higher score than stringB,
0, if they have the same score."""


def compare_scores(stringA, stringB):
    if not isinstance(stringA, str) or not isinstance(stringB, str):
        return None

    scoreA = get_score(stringA)
    scoreB = get_score(stringB)

    if scoreA < scoreB:
        return -1
    elif scoreA > scoreB:
        return 1
    else:
        return 0


"""Complete the function named factorial such that it returns 1 × 2 × ... × n. (If the input is 0, return 1. ) You may assume the input n is a non-negative integer.

Note: you must not use the for or while keywords."""


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(0))
"""Define a function longest_repeat that takes in a string, and returns the maximum number of times the same character appears consecutively."""


def longest_repeat(s):
    if not s:
        return 0

    max_count = 1
    current_count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 1

    return max_count


"""Define a function count_title_case that takes one string input, and returns the number of words that are in "title case".

A word is in title case if
the first character is an uppercase letter
all other characters are lowercase letters
(In the string "hello, world!", there are two words: "hello," and "world!". You can loop through them using "Hello, world!".split(" ") in Python.)"""


def count_title_case(s):
    count = 0
    for word in s.split(" "):
        if len(word) > 0 and word[0].isupper() and word[1:].islower():
            count += 1
    return count


def is_prime(n):
    """
    Takes an int n, with n >= 2,
    - returns True if it's a prime number (only factors are 1 and n)
    - returns False otherwise
    """
    oh_no = False
    for x in range(2, n):  # <-- at this line, 'oh_no' says whether any numbers we've checked are factors
        if is_multiple_of(n, x):
            oh_no = True
    # now, 'oh_no' says whether any of range(2,n) are factors
    return (not oh_no)


def is_prime2(n):
    for x in range(2, n):  # <-- at this line, 'oh_no' says whether any numbers we've checked are factors
        if is_multiple_of(n, x):
            return False
            # ('return' ends the function *immediately*)
    # if we get here, that means we didn't return False earlier
    return True


def is_multiple_of(n, divisor):
    """
    Takes two ints, both > 0.
    Returns True if n is a multiple of divisor.
    Returns False otherwise.
    """
    return (n % divisor == 0)


print(is_multiple_of(6, 4))  # expected answer: False
pear = is_multiple_of(10, 5)  # doesn't print anything
print(pear)  # expected answer: True
print(is_prime(35))

"""Define a function sum_ends_with_and_divisible that when passed 3 integers, (say n, val, divisor), returns the sum of all integers from 1 to n (inclusive) that end with the digit val and are divisible by divisor.

For example, if n = 50, val = 5, divisor = 3

The numbers that end with 5 and are divisible by 3 from 1 to 50 are 15, 35.

So, the sum would be 15 + 45 = 60."""
