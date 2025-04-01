import sys


def main():

    try:
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")

        filename = sys.argv[1]  # Confirms arg exists before checking syntax

        if not filename.endswith(".py"):
            sys.exit("Not a Python file")

        with open(filename) as file:
            contents = file.readlines()

    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        lines = get_lines(contents)
        print(lines)


def get_lines(contents):
    count = 0

    for line in contents:
        if not line.startswith("#") and line != "\n":
            count += 1

    return count


if __name__ == "__main__":
    main()
