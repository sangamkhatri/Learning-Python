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
