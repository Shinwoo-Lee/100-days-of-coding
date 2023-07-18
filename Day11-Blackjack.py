############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

###############################################################
from art import logo
import random
from replit import clear

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    return random.choice(deck)
  
def score(hand):
  hand_score = 0
  for card in hand:
    hand_score += card
  return hand_score
  
def burst(hand):
  if score(hand) > 21:
    return True
  else:
    return False

def result():
  if burst(computer):
    print("Opponent went over. You win 😁")
  elif score(player) == 21:
    print("Win with a Blackjack 😎")
  elif score(computer) == 21:
    print("Opponent went over. You win 😁")
  elif score(player) > score(computer):
    print("You win 😃")
  elif score(player) == score(computer):
    print("Draw 🙃")
  else:
    print("You lose 😭")

def hit_stand():
  hit_or_stand = input("Type 'y' to get another card, type 'n' to pass: ")
  if hit_or_stand == 'n':
    ### Stand ###
    while score(computer) < 17:
      computer.append(deal_card())
    print(f"   Your final hand: {player}, final score: {score(player)}")
    print(f"   Computer's final hand: {computer}, final score: {score(computer)}")
    result()
  else:
    ### Hit ###
    player.append(deal_card())
    print(f"   Your cards: {player}, current score: {score(player)}")
    print(f"   Computer's first card: {computer[0]}")
    if not burst(player):
      hit_stand()
    else:
      print(f"   Your final hand: {player}, final score: {score(player)}")
      print(f"   Computer's final hand: {computer}, final score: {score(computer)}")
      print("You went over. You lose 😭")


play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
while play_game == 'y':
  clear()
  print(logo)
  player = []
  computer = []
  player.append(deal_card())
  player.append(deal_card())
  computer.append(deal_card())
  computer.append(deal_card())
  print(f"   Your cards: {player}, current score: {score(player)}")
  print(f"   Computer's first card: {computer[0]}") 
  if burst(player):
    print(f"   Your final hand: {player}, final score: {score(player)}")
    print(f"   Computer's final hand: {computer}, final score: {score(computer)}")
    print("You went over. You lose 😭")
  else:
    hit_stand()
  play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
clear()
print("Good bye")