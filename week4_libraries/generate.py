# from random import choice  # Can create naming collisions with other modules
import random  # Allows you to make your own "choice" function

# coin = choice(["heads", "tails"])
coin = random.choice(["heads", "tails"])
print(coin)

number = random.randint(1, 10)  # inclusive, inclusive
print(number)

cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 19, "J", "Q", "K"]
# cards = ["jack", "queen", "king"]
random.shuffle(cards)
print(cards)
# for card in cards:
#     print(card)
