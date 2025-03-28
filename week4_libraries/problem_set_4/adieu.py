import inflect


def main():
    p = inflect.engine()
    names = []

    while True:
        try:
            name = input("Name: ").strip()

            if name != "":
                names.append(name)

        except EOFError:
            break

    print()
    if len(names) > 0:
        print(f"Adieu, adieu, to {p.join(names)}")
    else:
        print(f"Adieu, adieu, to no one")


main()
