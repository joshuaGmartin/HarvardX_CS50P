vowels = ["a", "e", "i", "o", "u"]


def main():
    tweet1 = twttrize("Twitter")
    tweet2 = twttrize("What's your name?")
    tweet3 = twttrize("CS50")
    print(tweet1)
    print(tweet2)
    print(tweet3)


def twttrize(text):
    tweet = ""

    for char in text:
        if char.lower() not in vowels:
            tweet += char

    return tweet


if __name__ == "__main__":
    main()
