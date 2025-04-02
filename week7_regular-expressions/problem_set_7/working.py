import re


def main():
    # workday = "9 AM to 5 PM"
    # workday = "9:00 AM to 5:00 PM"
    # workday = "9:00 AM to 5 PM"
    # workday = "9 AM to 5:00 PM"
    # workday = "13 AM to 5:00 PM"
    # workday = "9 AM to 5:60 PM"
    # workday = 123
    # workday = "cat"
    # workday = "9 AM - 5 PM"

    print(convert(workday))


def convert(workday):
    # increase number limits to allow manual raise ValueError?
    try:
        matches = re.match(
            r"([1-9]|1[0-2]):?([0-5][0-9])? ([A|P])M to ([1-9]|1[0-2]):?([0-5][0-9])? ([A|P])M$",
            workday,
        )

        start_hour, start_min, start_half, end_hour, end_min, end_half = (
            matches.groups()
        )
    except Exception:
        raise ValueError()  # this seems dumb

    # return (start_hour, start_min, start_half, end_hour, end_min, end_half)
    return format(start_hour, start_min, start_half, end_hour, end_min, end_half)


def format(start_hour, start_min, start_half, end_hour, end_min, end_half):
    # conform
    if start_min is None:
        start_min = "00"
    if end_min is None:
        end_min = "00"

    # Conform
    if start_half == "P":
        start_hour = str(int(start_hour) + 12)
    if end_half == "P":
        end_hour = str(int(end_hour) + 12)

    # CONFORM
    if int(start_hour) < 10:
        start_hour = "0" + start_hour
    if int(end_hour) < 10:
        end_hour = "0" + end_hour

    return f"{start_hour}:{start_min} to {end_hour}:{end_min}"


if __name__ == "__main__":
    main()
