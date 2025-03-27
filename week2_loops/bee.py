WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}


def main():
    print("Welcome to Spelling Bee!")
    print("Your letter are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word: ").upper()

        if guess == "GRAPHIC":
            WORDS.clear()
            print("SUPER WORD!")
        if guess in WORDS.keys():
            points = WORDS.pop(guess)
            print(f"Nice! You get {points} points")

    print("That's the game!")

    # for key, value in WORDS.items():
    # for word, points in WORDS.items():
    #     print(word, ": ", points, sep="")


main()
