distances = {"V1": "163", "V2": "136", "P10": "80 AU", "NH": "58", "P11": "44 AU"}


def main():

    # spacecraft = input("Enter spcacecraft: ")
    spacecraft = "Pxxx11"
    try:
        au = float(distances[spacecraft])
    except ValueError:
        print(f'Can\'t convert "{distances[spacecraft]}" to a float for {spacecraft}')
        return
    except KeyError:
        print(f'"{spacecraft}" is not in dictionary')
        return

    m = convert(au)
    print(f"{spacecraft} is {m}m away")


def convert(au):
    return au * 149597870700


main()
