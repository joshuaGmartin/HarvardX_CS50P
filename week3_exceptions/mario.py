def main():
    # height = int(input("Height: "))
    # pyramid(height)
    pyramid(5)


def pyramid(n):
    for i in range(n):
        print(" " * (n - (i + 1)), end="")
        print("#" * (i + 1))


main()
