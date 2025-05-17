"""Assume the existence of a function get_score that takes a single string input and returns an int.
(⚠️ get_score may crash if the inputs aren't strings!)

Complete the function compare_scores so that it returns...

None, if stringA or stringB are not strings.
-1, if stringA has a strictly lower score than stringB,
1, if stringA has a strictly higher score than stringB,
0, if they have the same score."""


def get_score(s):
    if not isinstance(s, str):
        print("Input must be a string")
    else:
        return sum(ord(char)for char in s)


def compare_scores(stringA, stringB):
    if not isinstance(stringA, str) and not isinstance(stringB, str):
        return None
    elif stringA < stringB:
        return -1
    elif stringA > stringB:
        return 1
    else:
        return 0


print(compare_scores("mouse", "mouse"))
print(compare_scores("mouse", "mous"))
print(compare_scores("mouse", "mouseee"))  # perfectly executed girl!
"""Complete the function named factorial such that it returns 1 × 2 × ... × n. (If the input is 0, return 1. ) You may assume the input n is a non-negative integer.

Note: you must not use the for or while keywords.

"""


def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)


print(factorial(0))  # 1
print(factorial(1))  # 1
print(factorial(4))  # 24
print(factorial(5))  # 120

"""Define a function longest_repeat that takes in a string, and returns the maximum number of times the same character appears consecutively."""


def longest_repeat(s):
    if not s:
        return 0

    max_count = 1
    current_count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 1

    return max_count


print(longest_repeat("aabbccdd"))        # 2
print(longest_repeat("aaabbbccaa"))      # 3
print(longest_repeat("abc"))             # 1
print(longest_repeat("aabbaaabbbaaaa"))  # 4
print(longest_repeat(""))                # 0

"""Define a function count_title_case that takes one string input, and returns the number of words that are in "title case".

A word is in title case if
the first character is an uppercase letter
all other characters are lowercase letters
(In the string "hello, world!", there are two words: "hello," and "world!". You can loop through them using "Hello, world!".split(" ") in Python.)"""


def count_title_case(text):
    count = 0
    for word in text.split(" "):
        # Remove punctuation at start and end
        word = word.strip(".,!?;:'\"-_()[]{}")
        if (
            word and
            word[0].isupper() and
            word[1:].islower() and
            word.isalpha()  # Ensures no digits, dots, hyphens, etc.
        ):
            count += 1
    return count


print(count_title_case("Pride and Prejudice"))              # 2 ✅
print(count_title_case("An Apple a Day"))                   # 3 ✅
print(count_title_case("HeLLO World?"))                     # 0 ✅
print(count_title_case("The Strange Case of Dr. Jekyll and Mr. Hyde"))  # 5 ✅
print(count_title_case("The 39 Steps"))                     # 2 ✅
print(count_title_case("A.b C_d E. F_ GhIJ"))
