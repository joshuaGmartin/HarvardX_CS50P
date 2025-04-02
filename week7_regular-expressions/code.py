import re


def main():
    # code = input("hex code: ")
    # code = "#AABBCC"
    # code = "#112233"
    # code = "112233"
    # code = "#GGGGGG"
    # code = "#11223G"
    # code = "#11223344"
    # code = "#aabbcc"
    # code = "#a|bbcc"
    code = "#1a2b3c"
    # code = "the hex code is #1a2b3c"

    # pattern = r"^#(([0-9A-F]{2}){3})$"
    pattern = r"^#([0-9A-F]{2})([0-9A-F]{2})([0-9A-F]{2})$"
    if codes := re.search(pattern, code, re.IGNORECASE):
        red, green, blue = codes.groups()
        print(red.upper(), green.upper(), blue.upper())
    else:
        print("Invalid hex code")


main()
