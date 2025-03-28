import random

cards = ["jack", "queen", "king"]


def main():
    # print(random.choices(cards, k=2))  # replace card
    # print(random.sample(cards, k=2))  # no replace
    # print(random.choices(cards, weights=[2, 1, 1], k=2))  # no replace

    random.seed(0)  # seed usually changes, like based on system time
    print(random.choices(cards, k=2))  # seed(0) always = [king, king]


main()
