# learning more strings manipulationa nd basic opeartions on string
# learning to take input from the python
# name = input("what is your name?")
# print("hi my name is ", name)
# slicing the string with index.
word = "Sangamkhatriissmartandintelligent"
print(word)
print(word[0:10:2])
print(word[2:10:3])

unit = "Foundation os Computer programmming"
code = "6010"
print("hi i am studying" + unit + "and its code is" + code)
print(len(word))
print(word.strip())
print(unit.replace("programming", "code"))
"""# Operators
# arithmatic Operators
2+3  # addition
2-3  # subtraction
2*3  # mulitplication
6/2  # division
6 % 3  # modulo or remiander
2**3  # power/exponentiation
15//2  # floor division (rounded)
# Python Bitwise Operators
2 and 3  # both has to be true or false.
2 or 3  # one can be either true or false to justify the result.
2 xor 3  # if both bits are same sets it to zero.
not  # inverts all the bits so convert 1 to 0 and vice versa.
# Python Assignment Operators
x = 5  # it doesnt mean equals to but is assigning a value 5 to x.
2 == 5  # double equals mean the both values are equal.
x -= 5  # subtraction 2 with x (x=x-5)
x += 5  # addition (x=x+5)
x /= 5  # division (x=x/5)
x *= 5  # mulitplication (x=x*5)
x!=5 #x is not equals to 5

#python Comaprison Operators
==  equals to
!= not equals to
>= greater or equal to
<= smaller or equal to
"""
num = 5
print(isinstance(num, float))
