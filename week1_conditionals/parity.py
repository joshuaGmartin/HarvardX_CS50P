def main():
    x = int(input("x?: "))
    if odd_checker(x):
        print("odd")
    else:
        print("even")


def odd_checker(n):
    # best
    return n % 2 != 0

    # better
    # return True if n % 2 != 0 else False

    # verbose
    # if n % 2 != 0:
    #     return True
    # return False


main()
