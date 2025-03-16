# def main():
#     difficulty = input("hard or easy?: ")
#     players = input("single or multi player?: ")

#     if difficulty == "hard":
#         if players == "multi":
#             recommed("Poker")
#         elif players == "single":
#             recommed("Klondike")
#         else:
#             print("invalid players")

#     elif difficulty == "easy":
#         if players == "multi":
#             recommed("Hearts")
#         elif players == "single":
#             recommed("Clock")
#         else:
#             print("invalid players")
#     else:
#         print("invalid difficulty")


# def recommed(game):
#     print("try", game)


# main()


# booleans
def main():
    difficulty = input("hard or easy?: ")
    if not (difficulty == "hard" or difficulty == "easy"):
        print("invalid difficulty")
        return

    players = input("single or multi player?: ")
    if not (players == "single" or players == "multi"):
        print("invalid players")
        return

    if difficulty == "hard" and players == "multi":
        recommed("Poker")
    elif difficulty == "hard" and players == "single":
        recommed("Klondike")
    elif difficulty == "easy" and players == "multi":
        recommed("Hearts")
    else:
        recommed("Clock")


def recommed(game):
    print("try", game)


main()
