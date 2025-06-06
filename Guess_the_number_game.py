"""Project: Guess the Number Game
 Goal:
Computer picks a random number between 1 and 100

You guess until you get it right

It tells you if your guess is too high or too low

Shows how many attempts you took"""
import random


def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100... Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(
                    f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number!")


# Run the game
guess_the_number()
