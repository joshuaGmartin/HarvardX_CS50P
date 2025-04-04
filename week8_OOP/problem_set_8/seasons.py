from datetime import date
import re
import sys
import inflect

p = inflect.engine()


def main():
    # birth_raw = "1990-02-14".strip()
    # birth_raw = "2023-04-03".strip()
    # birth_raw = "2023/04/03".strip()
    # birth_raw = "2023-04-99".strip()
    birth_raw = "Feburuary 2, 1990".strip()

    matches = re.search(r"^([0-9]{4})-([0-9]{2})-([0-9]{2})$", birth_raw)

    if not matches:
        sys.exit("Invalid date. Need YYYY-MM-DD")

    birth_data = []
    for group in matches.groups():
        birth_data.append(int(group))

    birth_date = date(int(birth_data[0]), int(birth_data[1]), int(birth_data[2]))

    diff_min = (date.today() - birth_date).days * 24 * 60

    print(p.number_to_words(diff_min, andword="").capitalize(), "minutes")


if __name__ == "__main__":
    main()
