# # variable/Data type/uppercase/Lower case
# # create variables and assigning.
alpha = 10
beta = 14
gamma = 4
alpha /= alpha
beta -= beta
gamma *= gamma
solution = alpha+beta+gamma
print(solution)
var1 = 4
var2 = 2
result = 5+2*(var1 ** var2)
print(result)
# # Assume the existence of a variable named bob, double the value of bob and then print the variable.
bob = 12
bob *= 2
print(bob)
# # Store the value 50 in a variable foo.
# Multiply foo by2
foo = 50
foo *= 2
print(foo)
"""we're focusing on "computational thinking"

 - *sequence* of doing things
- *selection* of what to do
 - *iteration*: doing something multiple times

 - ('software engineering' practices)

 Week 1:
 - output
 - different 'data types'
    - combining data together
    - conversion"""
print()  # prints the blank line
print("hakuna Matata")  # prints whatever is between the quotation
print(99)  # prints 99
# strings needed to be written inside quotation
# integer dont need to be written inside quotation
# this does print but dont recommend to join like this.
print("how" "are" "you" "?")
print("i am " + "sangam")  # this is concatenation
# recommened to join str like this as it looks cleaner
# doesnot join integer values
# we convert int values to str to use +
print("i am " + str(23) + " " + "years old")
print(-3*10)  # python prints direct operations as well
# data types
"""Python has integer,float,string and boolean as the data type
in Python, the four basic data types are:
- string (text, "hello world")
- int    (integer -- whole numbers. -3, 0, 1, 99...)
- float  (floating point numbers -- not necessarily whole numbers. 0.25, 99.346988)
- bool   (Boolean -- True, or False)"""
print(type(4))  # prints the data types the given number
print(type(4.5))
print(type(True))
print(type("sangam"))
# Variables (storing things for later use)
# storing sangam in name so that we can use name variable anywhere in the code.
name = "sangam"
age = 23
print(name, age)
# uppercase/Lowercase
print(name.lower())  # print the lower case
print(name.upper())  # print the upper case
