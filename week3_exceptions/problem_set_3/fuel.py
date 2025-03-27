def main():
    while True:
        ratio = input("Input fraction as X/Y: ").split("/")
        try:
            x = int(ratio[0])
            y = int(ratio[1])

            if x > y:
                # raise Exception("X may not be larger than Y")  # Exits program
                print("X may not be larger than Y")
                continue

            tank = get_tank(x, y)

        except ValueError:
            print("X and Y must be integers")
        except IndexError:
            print("Must enter fraction as X/Y")
        except ZeroDivisionError:
            print("Y may not be zero")
        else:
            print(tank)
            return


def get_tank(num, denom):
    tank = round(num / denom, 2) * 100
    if tank <= 1:
        return "E"
    elif tank >= 99:
        return "F"
    else:
        return str(tank) + "%"


main()
