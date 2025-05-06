# DAY 4 of Learning Python/Conditions(simple conditions)

# The following code should print "Positive" if the number is positive, otherwise print "Not positive".
num = 2
if num > 0:
    print("Positive")
else:
    print("negative")

# The following code should print "Odd" if the number is odd, otherwise print "Even".
n = 3
if n % 2 == 0:
    print("Even")
else:
    print("ODD")

# Assume the existence of three int variables a, b and c.

# Write some code that assigns the lowest value of a, b or c into a variable named lowest.
a = 2
b = 3
c = 4
if a < b and a < c:
    lowest = a
elif b < a and b < c:
    lowest = b
else:
    lowest = c
print(lowest)

# Assume the existence of a variable named study_hours. Print "Good" if the number of hours studied is 10 or more, "Okay" if the number of hours studied is between 5 and 10 (exclusive) and ":(" otherwise.
study_hours = 4
if study_hours >= 10:
    print("GOOD")
elif 5 < study_hours < 10:
    print("Okay")
else:
    print(":(")

"""Assume the existence of three variables x, y and z, write code that does one of the following:

increase z by 1 if both x and y are positive
decrease z by 1 if only x is positive, not y
increase z by 2 if only y is positive, not x
decrease z by 2 if neither x nor y are positive"""
x = -1
y = -2
z = 3
if x > 0 and y > 0:  # if both +ve
    z += 1
elif x > 0 and y < 0:
    z -= 1
elif y > 0 and x < 0:
    z += 2
else:
    z -= 2
print(z)

"""Assume the existence of a variable named age. Store in another variable called category, the values

"Child" if under 13
"Teen" if between 13 and 19
"Adult" otherwise. """

age = 20
if age < 13:
    category = "Child"
elif age >= 13 and age <= 19:
    category = "TEEN"
else:
    category = "Adult"
print(category)
"""Assume the existence of a variable named number. Store in a variable named result, 
"Positive Even" if number is positive and even
"Positive Odd" if number is positive and odd
"Negative Even" if number is negative and even
"Negative Odd" if number is negative and odd
"Number is 0" if number does not match any of the criteria above.
"""
number = 10
if num > 0 and num % 2 == 0:
    result = "Positive Even"
elif num > 0 and num % 2 != 0:
    result = "Positive Odd"
elif num < 0 and num % 2 == 0:
    result = "Negative Even"
elif num < 0 and num % 2 != 0:
    result = "Negative Odd"
else:
    result = "Number is 0"
print(result)
