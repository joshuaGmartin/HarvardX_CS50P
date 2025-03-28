import random


def main():
    level = get_level()
    rand_num = random.randint(1, level)

    play_game(rand_num)


def play_game(rand_num):
    while True:
        try:
            # must be int
            guess = int(input("Guess: "))

            # must be postive
            if guess > 0:
                result = check_guess(rand_num, guess)

                if result > 0:
                    print("Too high!")
                elif result < 0:
                    print("Too low!")
                else:
                    break

        except ValueError:
            pass

    print("Just right!")


def check_guess(rand_num, guess):
    return guess - rand_num


def get_level():
    while True:
        try:
            # must be int
            level = int(input("Level: "))

            # must be postive
            if level > 0:
                return level
        except ValueError:
            pass


if __name__ == "__main__":
    main()
