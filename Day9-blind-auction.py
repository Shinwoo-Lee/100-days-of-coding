from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.


def add_bid(dictionary):
    name = input("What is your name?: ")
    price = int(input("Whar is your bid?: $"))
    dictionary[name] = price


def check_winner(dictionary):
    winner = ""
    best_price = 0
    for name in dictionary:
        if dictionary[name] > best_price:
            winner = name
            best_price = dictionary[name]
    print(f"The winner is {winner} with a bid of ${best_price}")


continue_bidding = True
auction = {}

print(logo)

while continue_bidding:
    add_bid(auction)
    continue_auction = input(
        "Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if continue_auction == "yes":
        clear()
    elif continue_auction == "no":
        clear()
        check_winner(auction)
        continue_bidding = False
