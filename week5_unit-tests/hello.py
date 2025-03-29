def main():
    name = input("name?: ")
    print(hello(name))  # Print here


def hello(to="world"):
    # print("hello,", to)  # Good practice to return and  print elsewhere (cant test "print")
    return f"hello, {to}"


if __name__ == "__main__":
    main()
