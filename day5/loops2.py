# more of loop practice
"""Assuming the existence of a variable named temperature, write a piece of code that prints based on the following

"Wear a heavy jacket", if temperature is below 10
"Wear a jumper", if temperature is between 10 and 20
"A t-shirt is fine", if temperature is more than 20."""
if temperature < 10:
    print("Wear a heavy jacket")
elif 10 <= temperature <= 20:
    print("Wear a jumper")
else:
    print("A t-shirt is fine")

"""Write a loop that prints all numbers from 1 to 50(inclusive), that are not multiples of 3."""
for i in range(1, 51):
    if i % 3 != 0:
        print(i)
"""Count numbers between -35 to 45 (inclusive), that are multiples of 5 and store the answer in a variable called count_fives."""
count_fives = 0
for i in range(-36, 46):
    if i % 5 == 0:
        count_fives += 1
"""Calculate the sum of numbers between 30 to 72 (inclusive), that are multiples of 3 and 4, and store the answer in a variable called sum_multiples.
"""
sum_multiples = 0

for i in range(30, 73):  # includes 72
    if i % 3 == 0 and i % 4 == 0:
        sum_multiples += i
