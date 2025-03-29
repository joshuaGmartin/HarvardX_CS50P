import sys


def main():
    # fraction = get_fraction("5/4")
    fraction = get_fraction("4/5")
    # fraction = get_fraction()
    tank = get_tank(fraction[0], fraction[1])
    print(tank)


class SpecialException1(Exception):
    # when X > Y
    pass


def get_fraction(ratio=None):
    # Allows for testing
    if ratio == None:
        ratio = input("Input fraction as X/Y: ")
    ratio = ratio.split("/")

    # try:
    x = int(ratio[0])
    y = int(ratio[1])

    if x > y:
        # raise Exception("X may not be larger than Y")
        raise SpecialException1()

        # except SpecialException1:
        #     print("X may not be larger than Y")
        # except ValueError:
        #     print("X and Y must be integers")
        # except IndexError:
        #     print("Must enter fraction as X/Y")
        # except ZeroDivisionError:
        #     print("Y may not be zero")
        # else:
    return (x, y)


def get_tank(num, denom):
    tank = round(num / denom, 2) * 100
    if tank <= 1:
        return "E"
    elif tank >= 99:
        return "F"
    else:
        return str(tank) + "%"


if __name__ == "__main__":
    main()
