# conditions
"""Assume the existence of a variable named marks. Print "Unit passed" if marks are 50 or more."""
marks = 70
if marks >= 50:
    print("Unit Passed")
# Assume the existence of a variable named age. Print "Super unlocked" if age is over 65.
age = 65
if age > 64:
    print("Super unlocked")
# Assume the existence of a variable named  score. If score is greater than or equal to 100, add 25 to score.
score = 110
if score >= 100:
    score += 25
    print(score)
# Assume the existence of a variable named speed. Store "Speeding" in a variable named status is speed is greater than 80; otherwise, store "Safe Driving".
speed = 50
if speed >= 80:
    status = "Speeding"
else:
    status = "Safe Driving"
print(status)
# Assume the existence of a variable named temperature. Print "Hot" if the temperature is more than 25 degrees, otherwise print "Cold".
temperature = 10
if temperature >= 25:
    print("Hot")
else:
    print("Cold")
# The following code should print "Odd" if the number is odd, otherwise print "Even".
num = 2
if num % 2 == 0:
    print("even")
else:
    print("Odd")
