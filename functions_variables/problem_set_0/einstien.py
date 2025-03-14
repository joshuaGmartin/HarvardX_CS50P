def main():
    # mass = 1
    mass = int(input("Enter mass in kg (whole numbers only): "))
    print(energy(mass))


def energy(mass):
    return mass * 300000000**2


main()
