# def main():

#     try:
#         x = int(input("Enter number: "))
#     except ValueError:
#         print("Must enter integer")
#         main()
#     else:
#         print(f"x is {x}")


# main()

# =========================================
# while True:
#     try:
#         x = int(input("Enter number: "))
#         break
#     except ValueError:
#         print("Must enter integer")
#     # else:
#     #     break

# print(f"x is {x}")


# =========================================
def main():
    x = get_int("What's x?: ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            # print("Must enter integer")
            pass


main()
