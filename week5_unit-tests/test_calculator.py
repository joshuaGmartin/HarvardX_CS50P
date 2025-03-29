from calculator import square


def main():
    test_square()


def test_square():
    # if square(2) != 4:  # Error no trigger because 2 + 2 = 4, good to run multiple test
    #     print("2 squared was not 4")
    # if square(3) != 9:
    #     print("3 squared was not 9")

    # lots of code, use pytest
    try:
        assert square(2) == 4
    except AssertionError:
        print("2^2 was not 4")

    try:
        assert square(3) == 9
    except AssertionError:
        print("3^2 was not 9")

    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2^2 was not 4")

    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3^2 was not 9")

    try:
        assert square(0) == 0
    except AssertionError:
        print("0^2 was not 0")
    else:
        print("0^2 passed")


if __name__ == "__main__":
    main()
