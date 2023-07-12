rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

available = [rock, paper, scissors]
user_choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Scissors and 2 for Paper\n"
    ))
computer_choice = random.randint(0, 2)

if 0 <= user_choice <= 2:
    print(available[user_choice])
    print(f"Computer chose: {computer_choice}")
    print(available[computer_choice])

    if user_choice == computer_choice:
        print("Draw!")
    elif user_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose")
    elif user_choice < computer_choice:
        print("You Lose")
    else:
        print("You Win!")

elif user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
