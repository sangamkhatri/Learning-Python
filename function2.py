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
