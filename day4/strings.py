# Practicing String manupulation.
# Assume the existence of 2 string variables named first and second, write code to concatenate the two strings and store it in a variable called result.
first = "sangam"
second = "Khatri"
result = first + second
print(result)

"""Assume the existence of a variable animal that holds the value "{{ animal}}" and another variable sound that holds the value "{{ sound}}".
Concatenate them, with a space in between, and store the result in a third variable named animal_sound_mapping.
"""
animal = "{{animal}}"
sound = "{{sound}}"
animal_sound_mapping = animal + " " + sound
print(animal_sound_mapping)

# Assume the existence of a variable text, print the length of the string.
text = "sanga"
print(len(text))

# Assume the existence of a variable data. Create a new variable named information containing the type of the data variable
data = "Sangamji"
information = type(data)
print(information)

# Assume the existence of a variable text, print the string in lowercase/uppercase.

text = "Sangam SANGAM"
print(text.lower())
print(text.upper())

# Assume the existence of a variable text. Create a new variable named cleaned containing the string with all leading and trailing spaces removed.
cleaned = text.strip()
print(text)

# Assume the existence of a String variable data. Replace all occurrences of the word 'Python' with 'Java' in data and print it.
dat = "I love python.and i dont like python"
print(dat.replace("python", "java"))

"""Assume the existence of a String variable data. Replace all occurrences of 'red' with 'blue' in data and store the result in a variable named all_the_blues.
"""
dates = "The red car is red in color and i like the red color wow red."
print(dates.replace("red", "blue"))

"""Assume the existence of a String variable data. 

Replace all occurrences of "dog" (case-insensitive) with "cat" in data and store the result in a variable named check_that_out. The original value of data should not change."""
dataa = "DOG is barking,oh my dog."
dataa = data.lower()
print(dataa.replace("dog", "cat"))

# Assume the existence of a String variable data. Print every second character from index 1 (inclusive) to index 15 (exclusive).
da = "sangam is okay."
print(da[1:15:2])

# Assume the existence of a String variable data. Print every second character from index 0 (inclusive) to index 10 (exclusive).
print(da[0:10:2])

# Assume the existence of a String variable data. Print every third character starting from the 4th index (inclusive) to the 40th index (exclusive).
print(da[4:40:3])

# Assume the existence of a String variable data and an integer variable n. Print every n-th character, starting from index 2 to index 30.
n = 5
print(da[2:30:n])

# Assume the existence of a String variable data. Print the string in reverse.
datas = "sangam"
print(datas[::-1])

# Assume the existence of a String variable data. Print the string in reverse order, but only every fourth character, starting from index 50 down to index 10 (inclusive).
print(da[50:10:-4])

# Assume the existence of a String variable data. Reverse the characters from index 5 (inclusive) to index 15 (exclusive) and store it in a variable called reversed.
print(datas[15:5:-1])
