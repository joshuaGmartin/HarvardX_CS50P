months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    while True:
        date = input("Date (month-day-year): ")

        if "/" not in date and "," not in date:
            continue

        date = convert_date(date)

        if int(date[1]) > 31:
            print("Days are too large")
            continue
        if int(date[0]) > 12:
            print("Months are too large")
            continue
        else:
            break

    print(f"{date[2]}-{date[0]}-{date[1]}")


def convert_date(date):
    if "/" in date:
        return date.split("/")
    elif "," in date:
        date = date.split(" ")
        return [str(get_month(date[0])), date[1][:-1], date[2]]


def get_month(month):
    for i in range(len(months)):
        if months[i] == month:
            return i + 1


main()
