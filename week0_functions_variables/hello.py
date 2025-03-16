# -----------------------------------------
# example 1
# -----------------------------------------
# ask user for name
# name = input("What is your name? ").strip().title()
# # name = name.strip().title()

# # greet user
# print("Hello, ", end="")
# print(name, end="")
# print("!")

# print("Hello, ", name, "!", sep="")

# # f string
# print(f"Hello, {name}!")


# -----------------------------------------
# example 2
# -----------------------------------------
# print(f"Hello, {input('What is your name? ').strip().title()}!")


# -----------------------------------------
# example 3
# -----------------------------------------
# name = input("What is your name? ").strip().title()
# first, last = name.split(" ")

# print(f"Hello, {first}!")


# -----------------------------------------
# example 4
# -----------------------------------------
# def main():
#     name = input("What is your name?: ").strip().title()
#     hello(name)


# def hello(to="World"):
#     print("Hello,", to)


# main()


# -----------------------------------------
# example 5
# -----------------------------------------
# def main():

#     def add(x, y):
#         return x + y

#     print(add(3, 2))


# main()


# -----------------------------------------
# example 6
# -----------------------------------------
# # scopes
# def main():
#     guess = get_guess()
#     if guess == 50:
#         print("yep")
#     else:
#         print("nope")
#         # noice
#         main()


# def get_guess():
#     guess = int(input("enter guess: "))
#     return guess


# main()


# -----------------------------------------
# example 7
# -----------------------------------------
# def main():
#     greeting = greet("hello bob")
#     print("uhh...", greeting)


# def greet(input):
#     if "hello" in input:
#         return "hello to you!"
#     else:
#         return "huh?"


# main()


# -----------------------------------------
# example 8
# -----------------------------------------
# emoticon = "v.v"


# def main():
#     say("anyone there?")
#     global emoticon
#     emoticon = ":D"
#     say("oh hi!")


# def say(phrase):
#     print(phrase, emoticon)


# main()


# -----------------------------------------
# example 9
# -----------------------------------------
FILMS = [" Long john silver", "frankenstien", " the grapes of Wrath"]


def main():
    cleaned_shows = []
    for film in FILMS:
        cleaned_shows.append(film.strip().title())

    print(", ".join(cleaned_shows))


main()
