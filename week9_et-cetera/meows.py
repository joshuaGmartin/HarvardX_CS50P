# MEOWS = 3  # all caps = "please dont change constant"

# for _ in range(MEOWS):
#     print("meow")

# ============================================


# class Cat:
#     MEOWS = 3

#     def __init__(self): ...

#     def meow(self):
#         for _ in range(Cat.MEOWS):

#             print("meow")


# cat = Cat()
# cat.meow()


# ============================================


# Python is not a strongly written language; it dynamically figures out the type a variable is supposed to be
# Python itself does not enforce type
# can use mypy and type hints to help out with this
# run mypmy meows.py to check all type (gives error numer: int)


# n: type hint | ()-> annotated: returns nothing (mypy now catches)
# def meow(
#     n: int,
# ) -> None:
#     for _ in range(n):
#         print("meow")


# def meow(n: int) -> str:
#     # formal documentation format (restructured text, a form of markdown language, a third-party convention)
#     # format allows auto analysis and easy docs creation
#     """
#     Meow n times.

#     :param n: Number of time to meow
#     :type n: int
#     :raise TypeError: If n is not an int
#     :return: A string of n meows, one per line
#     :rtype: str
#     """
#     return "meow\n" * n


# # number: int = input("number: ")  # returns string
# number: int = int(input("Number: "))
# meows: str = meow(number)  # function does not return, only prints (returns None)
# print(meows, end="")


# # ============================================


# import sys

# # use flags in CLI: python3 meows.py -n 3
# if len(sys.argv) == 1:
#     print("meow")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("meow")

# else:
#     print("usage: meows.py")

# # def meows(n)


# ============================================

# useful for many args, and in any order
# python3 meows.py -h or --help for help info
# usage: meows.py [-h] [-n N]: [optional]
import argparse

parser = argparse.ArgumentParser(
    "Meow like a cat"
)  # constructor for a class that comes in argparse
parser.add_argument(
    "-n", default=1, help="Numnber of times to meow", type=int
)  # a method
args = parser.parse_args()  # looks at sys.argv automatically without importing sys

print(args)

# for _ in range(int(args.n)):
for _ in range(args.n):  # trust "type=int" in add_argument
    print("meow")
