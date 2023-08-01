import art
from game_data import data
import random
from replit import clear


def get_random():
  return random.choice(data)


def show_candidate(target1, target2):
  print(
    f"Compare A: {target1['name']}, a {target1['description']}, from {target1['country']}"
  )
  print(art.vs)
  print(
    f"Compare B: {target2['name']}, a {target2['description']}, from {target2['country']}"
  )
  print(f"Pssst... the answer is {answer}")


def get_answer():
  if targetA['follower_count'] > targetB['follower_count']:
    return 'A'
  else:
    return 'B'


### Game Starts Here ###
print(art.logo)
score = 0
correct = True
targetA = get_random()
targetB = get_random()

while correct:

  targetA = targetB
  targetB = random.choice(data)
  answer = get_answer()

  show_candidate(targetA, targetB)
  guess = input("Who has more followers? Type 'A' or 'B': ")
  if guess == answer:
    correct = True
  else:
    correct = False

  clear()
  print(art.logo)
  if correct:
    score += 1
    print(f"You're right! Current score: {score}.")
  else:
    print(f"Sorry, that's wrong. Final score: {score}")
