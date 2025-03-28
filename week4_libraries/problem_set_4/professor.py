import random


def main():
    level = get_level()
    play_game(level)


def play_game(level):
    num_of_probs = 10
    score = 0

    for _ in range(num_of_probs):
        if run_prob(level):
            score += 1

    print("Score:", score)


def run_prob(level):
    x = get_rand_int(level)
    y = get_rand_int(level)
    tries_left = 3

    while tries_left > 0:
        answer = input(f"{x} + {y} = ")

        # As opposed to using int(answer) and having to make excetions ValueErrors
        if answer == str(x + y):
            return True
        else:
            print("EEE")
            tries_left -= 1

    print("Answer =", x + y)
    return False


def get_rand_int(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


def get_level():
    while True:
        try:
            # must be int
            level = int(input("Level: "))

            # must be between 1 - 3
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass


main()
