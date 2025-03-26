def main():
    print("CS50", is_valid("CS50"), sep=" - ")
    print("CS05", is_valid("CS05"), sep=" - ")
    print("CS50P", is_valid("CS50P"), sep=" - ")
    print("PI3.14", is_valid("PI3.14"), sep=" - ")
    print("H", is_valid("H"), sep=" - ")
    print("OUTATIME", is_valid("OUTATIME"), sep=" - ")
    print("AA0AA", is_valid("AA0AA"), sep=" - ")
    print("AA111", is_valid("AA111"), sep=" - ")
    print("CS50?", is_valid("CS50?"), sep=" - ")


def is_valid(plate_str):
    if not 2 <= len(plate_str) <= 6:
        return "Invalid: wrong size"
    if not plate_str[0].isalpha() or not plate_str[1].isalpha():
        return "Invalid: first two chars must but be alpha"
    if first_num_is_zero(plate_str):
        return "Invalid: first num is zero"
    if has_special_char(plate_str):
        return "Invalid: has special char"
    if has_middle_number(plate_str):
        return "Invalid: has middle num"

    return "Valid"


def first_num_is_zero(string):
    past_first_num = False
    for char in string:
        if char.isdigit() and past_first_num == False:
            past_first_num = True
            if char == "0":
                return True

    return False


def has_special_char(string):
    for char in string:
        if not char.isalnum():
            return True

    return False


def has_middle_number(string):
    for i in range(len(string)):
        if i + 1 < len(string):
            if string[i].isdigit() and string[i + 1].isalpha():
                return True

    return False


main()
