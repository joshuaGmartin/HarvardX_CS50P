import re

locations = {"+1": "US or Canada", "+62": "Indonesia", "+505": "Nicaragua"}


def main():
    pattern = r"^(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}$"  # capture group ref
    # number = input("phone number: ")
    # number = "+1 123-123-1234"
    # number = "+62 123-123-1234"
    number = "+505 123-123-1234"
    # number = "+1 (123) 123-1234"
    # number = "+1 123-123-12345"
    # number = "123-123-1234"

    if match := re.search(pattern, number):
        country_code = match.group("country_code")
        print("Call from:", locations[country_code])
    else:
        print("Invalid")


main()
