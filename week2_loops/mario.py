# mario bricks
# print("#")
# print("#")
# print("#")


def main():
    print_column(3)
    print_rows(4, "?")
    print_square(3)


def print_column(height):
    # for _ in range(height):
    #     print("#")
    print("#\n" * height, end="")


def print_rows(width, symbol):
    print(symbol * width)


def print_square(size):
    # for i in range(size):
    #     print("#" * size)

    for _ in range(size):
        print_rows(size, "#")

    # for i in range(size):  # For each row in square
    #     for j in range(size):  # For each brink in square
    #         print("#", end="")  # Print le brick
    #     print()  # New line for each row


main()


def print_pyramid(rows):
    num_Xs = 1
    num_spaces = rows - 1
    for i in range(rows):
        for _ in range(num_spaces):
            print(" ", end="")
        for _ in range(num_Xs):
            print("x", end="")
        print()
        # updates
        num_spaces -= 1
        num_Xs += 2


print_pyramid(10)
