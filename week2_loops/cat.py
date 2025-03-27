# ============================
# print("meow")
# print("meow")
# print("meow")

# ============================
# i = 3
# while i > 0:
#     print("meow")
#     i -= 1

# ============================
# i = 0
# while i < 3:
#     print("meow")
#     i += 1


# ============================
# for i in [1, 1, 1]:
# for i in [0, 1, 2]:
#     print("meow")

# ============================
# default range start = 0
# for i in range(3):
#     print("meow")

# ============================
# using "_" is the common name for a variable that must exist but is not used (means: "doesn't matter")
# for _ in range(3):
#     print("meow")

# ============================
# print("meow\n" * 3, end="")

# ============================
# n = 0
# # while n <= 0:
# #     n = int(input("How many meows?: "))
# while True:
#     n = int(input("How many meows?: "))
#     # if n <= 0:
#     #     continue
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")


# ============================
def main():
    number = getNumber()
    meow(number)


def meow(n):
    for _ in range(n):
        print("meow")


def getNumber():
    while True:
        n = int(input("How many meows?: "))
        if n > 0:
            return n


main()
