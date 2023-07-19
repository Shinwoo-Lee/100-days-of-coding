import random
from art import logo


def check_gameover(attempt):
    if attempt == 0:
        print("You've run out of guesses, you lose.")
    else:
        print("Guess agin")


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

answer = random.randint(1, 100)
# print(f"[ANSWER = {answer}]")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
attempt = 0

if difficulty == "easy":
    attempt = 10
elif difficulty == 'hard':
    attempt = 5
else:
    print("Wrong choice! Try again.")
    attempt = 0

while attempt != 0:
    print(f"You have {attempt} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > answer:
        print("Too high.")
        attempt -= 1
        check_gameover(attempt)
    elif guess < answer:
        print("Too low.")
        attempt -= 1
        check_gameover(attempt)
    else:
        print(f"You got it! The answer was {answer}.")
        attempt = 0
