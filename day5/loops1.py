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
