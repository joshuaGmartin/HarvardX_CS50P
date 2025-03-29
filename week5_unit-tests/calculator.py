def main():
    x = input("enter x: ")
    print("x^2 =", square(x))


def square(n):
    # return n + n  # sim error
    return n * n


if __name__ == "__main__":
    main()
