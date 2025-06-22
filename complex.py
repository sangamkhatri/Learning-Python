# 🧠 Complex Python Basics – All in One

# 1. Palindrome Checker with Filtering
def is_clean_palindrome(text):
    clean = ''.join(char.lower() for char in text if char.isalnum())
    return clean == clean[::-1]

# 2. Nested List Flattening using Recursion


def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# 3. Character Frequency Counter


def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

# 4. Custom FizzBuzz Function


def custom_fizzbuzz(limit, rules):
    for i in range(1, limit + 1):
        result = ''
        for num, word in rules.items():
            if i % num == 0:
                result += word
        print(result or i)

# 5. Class-Based Bank Account System


class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def show_balance(self):
        print(f"{self.name}'s balance: ${self.balance}")

# ---------------- RUNNING EVERYTHING ----------------


# Palindrome Check
text = "A man, a plan, a canal: Panama"
print("🔁 Palindrome Check:", is_clean_palindrome(text))

# Flatten Nested List
nested = [1, [2, [3, 4], 5], 6]
print("🧩 Flattened List:", flatten(nested))

# Character Frequency
word = "programming"
print("🔤 Character Frequency:", char_frequency(word))

# Custom FizzBuzz
print("🎯 Custom FizzBuzz (1 to 15):")
custom_fizzbuzz(15, {3: "Fizz", 5: "Buzz"})

# Bank Account Simulation
print("🏦 Bank Account Simulation:")
acc = BankAccount("Sangam")
acc.deposit(200)
acc.withdraw(50)
acc.show_balance()
# 🧠 Advanced Python Basics - Part 2

# 1. Password Strength Checker


def check_password_strength(password):
    import string
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
        return "Strong"
    elif len(password) >= 6:
        return "Medium"
    else:
        return "Weak"

# 2. Prime Number Finder


def find_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for div in range(2, int(num**0.5) + 1):
            if num % div == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# 3. Class Inheritance: Employee and Manager


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        return f"Employee: {self.name}, Salary: ${self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def show(self):
        return f"Manager: {self.name}, Salary: ${self.salary}, Team size: {self.team_size}"

# 4. Anagram Checker


def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

# 5. Number Pattern Printer (Triangle)


def print_number_triangle(n):
    for i in range(1, n + 1):
        print(" ".join(str(x) for x in range(1, i + 1)))

# ---------------- RUNNING THEM ----------------


# Password Strength
print("\n🔒 Password Strength:")
print("Password 'Hello@123':", check_password_strength("Hello@123"))

# Prime Numbers up to 30
print("\n🔢 Primes up to 30:")
print(find_primes(30))

# Employee vs Manager
print("\n👥 Employee and Manager Info:")
e = Employee("Alice", 50000)
m = Manager("Bob", 80000, 5)
print(e.show())
print(m.show())

# Anagram Check
print("\n🔁 Anagram Check ('listen', 'silent'):")
print(is_anagram("listen", "silent"))

# Number Triangle
print("\n🔺 Number Triangle Pattern (n=5):")
print_number_triangle(5)
