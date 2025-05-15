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
