def main():
    variable1 = snake_case("name")
    print(variable1)
    variable2 = snake_case("firstName")
    print(variable2)
    variable3 = snake_case("preferredFirstName")
    print(variable3)


def snake_case(camelCase):
    snake_case = ""

    for char in camelCase:
        if not char.islower():
            char = char.lower()
            snake_case = snake_case + "_"
        snake_case = snake_case + char

    return snake_case


main()
