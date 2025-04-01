from tabulate import tabulate
import csv
import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            table = [row for row in reader]
            print(tabulate(table, headers="keys", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()

# ======================================================

# def main():

#     with open("sicilian.csv", "r") as file:
#         contents = file.readlines()
#         table = []

#         for line in contents:
#             table.append(line.rstrip().split(","))

#         print(tabulate(table, headers="firstrow", tablefmt="grid"))


# if __name__ == "__main__":
#     main()
