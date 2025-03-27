grocery_list = {}


def main():

    while True:
        try:
            item = input("")
            add_item(item)
        except EOFError:
            print()
            break

    print_list()


def add_item(item):
    # if not item in grocery_list:
    if item not in grocery_list:
        grocery_list.update({item: 1})
    else:
        grocery_list[item] += 1


def print_list():
    for item in grocery_list.items():
        print(f"{item[1]} {item[0].upper()}")


main()
