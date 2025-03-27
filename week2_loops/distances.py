distances = {"V1": 163, "V2": 136, "P10": 80, "NH": 58, "P11": 44}


def main():
    # for key in distances:
    #     print(key)

    # for name in distances.keys():
    #     print(f"{name} is {distances[name]} AU from Earth")

    for distance in distances.values():
        print(f"{distance} AU is {convert(distance)} m")


def convert(au):
    return au * 149597870700


main()
