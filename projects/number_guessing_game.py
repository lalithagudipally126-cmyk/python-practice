import random

print("🎲 Welcome to the Number Guessing Game!")
number = random.randint(1, 20)   # computer picks a number between 1 and 20
attempts = 0
#random.randint(start,end) is the syntax for generating a random integer between the specified start and end values (inclusive).

while True:
    guess = int(input("Guess a number between 1 and 20: "))
    attempts += 1
#attempts += 1 is a shorthand way of writing attempts = attempts + 1. It increments the value of the variable attempts by 1 each time the loop runs, effectively counting the number of guesses the player has made.
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct! The number was {number}.")
        print(f"You guessed it in {attempts} attempts.")
        break
