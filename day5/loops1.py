# here we are learning loops basics
for i in range(5):  # the code runs for 5 times
    print(i)
sum = 0
for i in range(2, 5):  # it give range to run the loop from 2 inclusive to 5 exclusive
    sum += i
    print(sum)
for i in range(1, 13, 3):  # this give sthe range as well the steps .
    print(i)
for i in range(3, 10):  # prints all between the range that is divisible by 2.
    if i % 2 == 0:
        print(i)
x = 1
for i in range(10, 4, -2):
    x *= i
print(x)
text = "HELLO!"  # prints the letters in text from the beginning till its length
for i in range(len(text)):
    print(text[i])
total = 1
for i in range(1, 4):
    for j in range(1, 3):
        total += i*j
        print(total)
count = 0
for i in range(1, 5):  # the range is (1,2,3,4)
    for j in range(i):  # when i =1 ,j range between 0,1 that is j=0
        print(i, j)  # when i=2,j ranges from 0,2 that is 0 and 1 and the rest follows
result = 3
counter = 6
while counter < 55:  # while counter is less than 55 the loop runs
    result = result+3  # as long as counter is less than 55 it adds 3 to existing result
    # and adds the counter by 7 with every loop and again checks if counter is less than 55
    counter = counter+7
    print(result)
# Write a loop which will print every number from 10 (inclusive) to 64 (inclusive) in steps of 6.
for i in range(10, 65, 6):
    print(i)
# The following code attempts to prints all numbers from 10 to 20 (inclusive of both. But there is a problem with the code.
for i in range(10, 21):
    print(i)
# The following code attempts to prints all numbers from 0 to 9. But there is a problem with the code.
# Click the Check button to identify the problem and fix it.
for i in range(0, 10):
    print(i)
# Write a loop which will print every number from 70 (inclusive) to 182 (inclusive) in steps of 7 using a while loop.
x = 70
while x <= 182:
    print(x)
    x += 7
# Write a for loop which will print every number from 1 (inclusive) to 26 (exclusive) in steps of 3.
for i in range(1, 26, 3):
    print(i)
# Write a loop which will print every number from 100 (inclusive) to 251 (exclusive) in steps of 5 using a for loop.
for i in range(100, 251, 5):
    print(i)
# Assume the existence of variable named first. Write a loop which will print every number from first(inclusive) to 50(exclusive) in steps of 4.
first = 2
for i in range(first, 50, 4):
    print(i)
# Assume the existence of two variables named first and last. Write a loop which will print every number from first(inclusive) to last(exclusive) in steps of 3.
first = 2
last = 5
for i in range(first, last, 1):
    print(i)
"""Write a piece of Python code that prints a newline-separated sequence with the following parameters:

First value to print 	17
Step (difference between an item and the previous item)     	6
Number of items in the sequence	35

So, the output should be:

17
23
29
... (these signify a continuation in the pattern)
222"""
start = 17
step = 6
num = 35
for i in range(num):
    print(start+i*step)
"""Write a piece of Python code that prints a newline-separated sequence with the following parameters:

Purpose 	Value
First value to print 	1729
Step (difference between an item and the previous item)     	-12
Number of items in the sequence	108

So, the output should be:

1729
1717
1705
... (these signify a continuation in the pattern)
445
"""
start = 1729
step = -12
num = 108
for i in range(num):
    print(start+i*step)
""" Complete the  code using a nested loop that prints the following pattern -
# # # #
# # # #
# # # #"""
for i in range(3):        # 3 rows
    for j in range(5):    # 5 columns
        print("#", end=" ")  # print on same line with space
    print()               # move to next line after each row
"""The code provided uses a nested loop to prints the following pattern -
$ $ $ $ $

$ $ $ $ $

$ $ $ $ $

$ $ $ $ $"""
for i in range(4):
    for j in range(5):
        print("$", end=" ")
    print()
"""Write a nested loop that prints the following pattern -

^ ^ ^ ^
^ ^ ^ ^
^ ^ ^ ^
^ ^ ^ ^
^ ^ ^ ^
^ ^ ^ ^ """
for i in range(6):
    for j in range(4):
        print("^", end=" ")  # prints in a single line with spaces.
    print()
"""Write a nested loop that prints the following pattern -

14 18 22 26

30 34 38 42

46 50 54 58

62 66 70 74

78 82 86 90"""
start = 14
steps = 4
for i in range(5):
    for j in range(4):
        print(start, end=" ")
        start += steps
    print()
"""Write a nested loop that prints the following pattern -

10 13 16 19 22 25 28 31

10 13 16 19 22 25 28 31

10 13 16 19 22 25 28 31

10 13 16 19 22 25 28 31

10 13 16 19 22 25 28 31"""
step = 3
for i in range(5):
    start = 10  # we use it inside the lopp so that everytime next line runs value starts from 10
    for j in range(8):
        print(start, end=" ")
        start += step
    print()
"""Write a nested loop that prints the following pattern -

85 80 75 70 65 60 55

50 45 40 35 30 25 20

15 10 5 0 -5 -10 -15
"""
start = 85
step = -5
for i in range(3):
    for j in range(7):
        print(start, end=" ")
        start += step
    print()
