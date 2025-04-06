def main():
    yell("This", "is", "CS50")


# def yell(*words):  # just pass in any number of args
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())

#     print(*uppercased)  # unpack


# def yell(*words):
#     # access str class to pass upper() method to words arg, return new list
#     uppercased = map(str.upper, words)
#     print(*uppercased)


# even better: list comprehension
def yell(*words):
    uppercased = [word.upper() for word in words]  # Pythonic
    print(*uppercased)


if __name__ == "__main__":
    main()
