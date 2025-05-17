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
